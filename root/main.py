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
from utility.warframeUtil import GetWarframeApp

moduleMapping = {
    "weather": lambda configs, container: GetWeatherApp(configs, container),
    "warframe": lambda configs, container: GetWarframeApp(configs, container)
}

class Win(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Python GUI")
        self.resizable(1,1)
        self.geometry('650x350')
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
    for module in kwargs['module']:
        if module in moduleMapping:
            moduleApp = moduleMapping[module](root.configs,
                                              getattr(root.tabContainer, module))
            modules.append(moduleApp)
    return modules

def main(*args, **kwargs):
    root = Win(*args, **kwargs)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    modules = runModule(root, *args, **kwargs)
    root.mainloop()

def on_closing(root):
    with root.configs.condition:
        root.configs.isStopped = True
        root.configs.condition.notify_all()
    root.quit()
    root.destroy()
    

if __name__ == '__main__':
    sys.setrecursionlimit(6000)
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--module', type=str, nargs='*')
    args = parser.parse_args()
    module = args.module
    if module == None:
        main(module=['main', 'weather', 'warframe'])
    else:
        main(module=args.module)
