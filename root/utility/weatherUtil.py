import threading
import datetime
import time
import os
import pickle
from tkinter import ttk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GetWeatherApp(threading.Thread):
    def __init__(self, configs, container):
        super().__init__()
        self.setDaemon(True)
        self.container = container
        self.configs = configs
        
        options_Args = ["--headless", "disable-gpu"]
        self.options = Options()
        for arg in options_Args:
            self.options.add_argument(arg)
        self.service_args = ["hide_console", ]
        self.DriverPath = __file__.rsplit(os.sep,1)[0] + r'\applications\chromedriver.exe'
        self.currentPath = __file__.rsplit(os.sep,1)[0]
        
        self.start()

    def checkWarningTextCache(self):
        warningText = None
        mtime = None
        try:
            mtime = os.path.getmtime(self.currentPath+r"\cache\warningText.txt")
            mtime = datetime.datetime.fromtimestamp(mtime)
        except:
            pass
        if mtime == None or ((datetime.datetime.now() - mtime).total_seconds() > 3600):
            warningText = self.getWarning("https://www.hko.gov.hk/wxinfo/dailywx/wxwarntoday_uc.htm")
            with open(self.currentPath+"\cache\warningText.txt", "wb") as warningTextFile:
                pickle.dump(warningText, warningTextFile)
        else:
            with open(self.currentPath+"\cache\warningText.txt", "rb") as warningTextFile:
                warningTextCache = pickle.load(warningTextFile)
                warningText = warningTextCache
        return warningText

    def checkWeatherResultDictCache(self):
        weatherResultDict = None
        mtime = None
        try:
            mtime = os.path.getmtime(self.currentPath+r"\cache\weatherResultDict.txt")
            mtime = datetime.datetime.fromtimestamp(mtime)
        except:
            pass
        if mtime == None or ((datetime.datetime.now() - mtime).total_seconds() > 3600):
            weatherResultDict = self.getWeather("https://www.hko.gov.hk/contentc.htm")
            with open(self.currentPath+r"\cache\weatherResultDict.txt", "wb") as weatherResultDictFile:
                pickle.dump(weatherResultDict, weatherResultDictFile)
        else:
            with open(self.currentPath+r"\cache\weatherResultDict.txt", "rb") as weatherResultDictFile:
                weatherResultDictCache = pickle.load(weatherResultDictFile)
                weatherResultDict = weatherResultDictCache
        return weatherResultDict
    
    def run(self):
        while not self.configs.isStopped:
            warningText = self.checkWarningTextCache()
            weatherResultDict = self.checkWeatherResultDictCache()
            with self.configs.condition:
                if not self.configs.isStopped:
                    r = self.showTime(0)
                    r = self.updateWarning(r, warningText)
                    r = self.updateWeather(r, weatherResultDict)
                    self.configs.condition.wait(3600)

    def showTime(self, startingRow):
        r = startingRow
        t = datetime.datetime.now().isoformat(sep=" ", timespec='seconds')  
        ttk.Label(self.container, text=t).grid(column=0, row=r, sticky='W')
        return r+1
    
    def updateWarning(self, startingRow, warningText):
        r = startingRow
        if warningText != []:
            text = " ".join(warningText)
            ttk.Label(self.container, text=text).grid(column=0, row=r, sticky='W')
            r += 1
        return r

    
    def updateWeather(self, startingRow, weatherResultDict):
        r = startingRow
        ttk.Label(self.container, text="日期").grid(column=0, row=r, sticky='W')
        ttk.Label(self.container, text="最低温度").grid(column=1, row=r, sticky='W')
        ttk.Label(self.container, text="最高温度").grid(column=2, row=r, sticky='W')
        ttk.Label(self.container, text="天氣簡述").grid(column=3, row=r, sticky='W')
        r+=1
        for key in weatherResultDict:
            text =[key, weatherResultDict[key][0], weatherResultDict[key][1], weatherResultDict[key][2]]
            for index in range(4):
                ttk.Label(self.container, text=text[index]).grid(column=index, row=r, sticky='W')
            r+=1
        return r

    def getWarningScrape(self,html):
        warningText = []
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.select(".style10 tbody tr td a img")
        for tag in tags:
            if tag.attrs['src'].endswith("issuing.gif"):
                warningText.append(tag.attrs['alt'])
        return warningText

    def getWarning(self, url):
        browser = webdriver.Chrome(self.DriverPath,service_args=self.service_args, options=self.options, )
        browser.get(url)
        result = self.getWarningScrape(browser.page_source)
        browser.quit()
        return result

    def getWeatherScrape(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.findAll(True, {'class':['fnd_date', 'fnd_min', 'fnd_max']})
        tags = [tag.text for tag in tags]
        descs = soup.select(".fnd_wxicon a img")
        desc = [desc.attrs['title'] for desc in descs]
        value = tuple(zip(tags[1::3], tags[2::3], desc))
        return dict(zip(tags[::3], value))
     
    def getWeather(self, url):
        browser = webdriver.Chrome(self.DriverPath,service_args=self.service_args, options=self.options, )
        browser.get(url)
        result = self.getWeatherScrape(browser.page_source)
        browser.quit()
        return result
