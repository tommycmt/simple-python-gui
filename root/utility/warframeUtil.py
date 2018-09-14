import threading
from datetime import datetime, timedelta
import time
import os
import pickle
import logging
from tkinter import ttk
from bs4 import BeautifulSoup
from .requestHTMLUtil import requestHTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GetWarframeApp(threading.Thread):
    def __init__(self, configs, container):
        super().__init__()
        self.setDaemon(True)
        self.container = container
        self.configs = configs
        self.currentPath = __file__.rsplit(os.sep,1)[0]  
        self.start()


    def checkWarframeResultDictCache(self):
        warframeResultDict = None
        mtime = None
        try:
            mtime = os.path.getmtime(self.currentPath+r"\cache\warframeResultDict.txt")
            mtime = datetime.fromtimestamp(mtime)
        except:
            pass
        if mtime == None or ((datetime.now() - mtime).total_seconds() > 600):
            warframeResultDict = requestHTML("http://wf.poedb.tw/", self.getWarframeScrape)
            with open(self.currentPath+r"\cache\warframeResultDict.txt", "wb") as warframeResultDictFile:
                pickle.dump(warframeResultDict, warframeResultDictFile)
        else:
            with open(self.currentPath+r"\cache\warframeResultDict.txt", "rb") as warframeResultDictFile:
                warframeResultDictCache = pickle.load(warframeResultDictFile)
                warframeResultDict = warframeResultDictCache
        return warframeResultDict
    
    def run(self):
        while not self.configs.isStopped:
            warframeResultDict = self.checkWarframeResultDictCache()
            logging.debug(warframeResultDict)
            with self.configs.condition:
                if not self.configs.isStopped:
                    for widget in self.container.winfo_children():
                        widget.destroy()
                    r = self.showTime(0)
                    r = self.updateWarframe(r, warframeResultDict)
                    self.configs.condition.wait(600)

    def showTime(self, startingRow):
        r = startingRow
        t = datetime.now().isoformat(sep=" ", timespec='seconds')  
        ttk.Label(self.container, text=t).grid(column=0, row=r, sticky='W')
        return r+1
    
    def updateWarframe(self, startingRow, warframeResultDict):
        r = startingRow
        ttk.Label(self.container, text="警報").grid(column=0, row=r, sticky='W')
        r+=1
        for alert in warframeResultDict["alerts"]:
            ttk.Label(self.container, text=alert[0]).grid(column=0, row=r, sticky='W')
            ttk.Label(self.container, text=alert[1].strftime("%H:%M:%S")).grid(column=1, row=r, sticky='W')
            for index in range(2, len(alert[2:]) + 2):
                ttk.Label(self.container, text=alert[index]).grid(column=index, row=r, sticky='W')
            r+=1
        ttk.Label(self.container, text="\n入侵").grid(column=0, row=r, sticky='W')
        r+=1
        for invasion in warframeResultDict["invasions"]:
            ttk.Label(self.container, text=invasion[0]).grid(column=0, row=r, sticky='W')
            r+=1
            for index in range(len(invasion[1:])):
                ttk.Label(self.container, text=invasion[index+1]).grid(column=1-index, row=r, sticky='W')
            r+=1
        return r


    def getWarframeScrape(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        result = dict()
        result['alerts'] = list()
        result['invasions'] = list()
        alertTags = soup.select("#alerts2 tbody tr td")
        for alertTag in alertTags:
            alertRewardTags = alertTag.select(".badge")
            endTime = datetime.fromtimestamp(int((alertTag.select(".end_time")[0])
                                                             .attrs["data-countdown"]))
            alert = [alertTag.select(".end_time")[0].next_sibling,
                     endTime]
            alertRewards = []
            currentTag = alertTag.select("hr")[0]
            while currentTag.next_sibling != None:
                currentTag = currentTag.next_sibling
                if currentTag.string.strip() != '':
                    alertRewards.append(currentTag.string)
            alert += alertRewards
            result['alerts'].append(alert)
        
        invasionTags = soup.select("#invasion2 tbody tr td")
        for invasionTag in invasionTags:
            invasionRewardTags = invasionTag.select(".badge")
            invasion = [invasionTag.contents[0]] + \
                        [invasionRewardTag.text for invasionRewardTag in invasionRewardTags if invasionRewardTag.text != '']
            result['invasions'].append(invasion)
        return result

