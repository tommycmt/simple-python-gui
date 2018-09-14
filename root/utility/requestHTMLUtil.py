import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def requestHTML(url, scraper):
    options_Args = ["--headless", "disable-gpu", "--no-sandbox"]
    options = Options()
    for arg in options_Args:
        options.add_argument(arg)
    service_args = ["hide_console", ]
    DriverPath = __file__.rsplit(os.sep,1)[0] + r'\applications\chromedriver.exe'
    browser = webdriver.Chrome(DriverPath,service_args=service_args, options=options, )
    browser.get(url)
    result = scraper(browser.page_source)
    browser.quit()
    return result

