from tkinter import ttk
import threading
import datetime
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GetWeatherApp(threading.Thread):
    def __init__(self, configs, mainTabContainer):
        super().__init__()
        self.setDaemon(True)
        self.mainTabContainer = mainTabContainer
        self.configs = configs
        self.start()

    def run(self):
        while not self.configs.isStopped:
            self.updateWeather()
            with self.configs.condition:
                self.configs.condition.wait(30)
    
    def updateWeather(self):
        weatherResultDict = self.getWeather()
        r = 0
        t = datetime.datetime.now()
        with self.configs.condition:
            if not self.configs.isStopped:
                ttk.Label(self.mainTabContainer, text=t).grid(column=0, row=r, sticky='W')
                r+=1
                for key in weatherResultDict:
                    text = "{}\t{}\t{}\t{}".format(key,weatherResultDict[key][0], weatherResultDict[key][1], weatherResultDict[key][2])
                    ttk.Label(self.mainTabContainer, text=text).grid(column=0, row=r, sticky='W')
                    r+=1

    def getWeatherScrape(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.findAll(True, {'class':['fnd_date', 'fnd_min', 'fnd_max']})
        tags = [tag.text for tag in tags]
        descs = soup.select(".fnd_wxicon a img")
        desc = [desc.attrs['title'] for desc in descs]
        value = tuple(zip(tags[1::3], tags[2::3], desc))
        return dict(zip(tags[::3], value))
     
    def getWeather(self):
        url = 'https://www.hko.gov.hk/contentc.htm'
        service_args = ["hide_console", ]
        options_Args = ["--headless", "disable-gpu"]
        DriverPath = r'utility\applications\chromedriver.exe'
        options = Options()
        for arg in options_Args:
            options.add_argument(arg)
        browser = webdriver.Chrome(DriverPath,service_args=service_args, options=options, )
        browser.get(url)
        result = self.getWeatherScrape(browser.page_source)
        browser.quit()
        return result

        
