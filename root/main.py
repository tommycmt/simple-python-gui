import sys, os
import argparse
import threading
import tkinter as tk
from tkinter import ttk
from config.config import Config
from component.menubar import Menubar
from component.tabControl import TabControl
from component.tabContainer import TabContainer

from utility.weatherUtil import GetWeatherApp

class Win(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Python GUI")
        self.resizable(1,1)
        self.geometry('450x250')
        condition = threading.Condition()
        self.configs = Config(condition)
        self.configUI(*args, **kwargs)

    def configUI(self, *args, **kwargs):
        def configMenubar():
            self.config(menu=Menubar(self))

        def configTabControl(*args, **kwargs):
            self.tabControl = TabControl(self, *args, **kwargs)

        def configTabContainer(*args, **kwargs):
            self.tabContainer = TabContainer(self, *args, **kwargs)
            
        configMenubar()
        configTabControl(*args, **kwargs)
        configTabContainer(*args, **kwargs)
        
def runModule(root, *args, **kwargs):
    modules = []
    if ('weather' in kwargs['module']):
        weatherApp = GetWeatherApp(root.configs, root.tabContainer.weather)
        modules.append(weatherApp)
    return modules

def main(*args, **kwargs):
    root = Win(*args, **kwargs)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    modules = runModule(root, *args, **kwargs)
    root.mainloop()

def on_closing(root):
    with root.configs.condition:
        print(root.configs.condition)
        print(root.configs.isStopped)
        root.configs.isStopped = True
        root.configs.condition.notify_all()
    root.quit()
    root.destroy()
    print(root.configs.condition)
    print(root.configs.isStopped)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--module', type=str, nargs='*')
    args = parser.parse_args()
    module = args.module
    if module == None:
        main(module=['main', 'weather', 'warframe'])
    else:
        main(module=args.module)
