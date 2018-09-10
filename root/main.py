import tkinter as tk
from tkinter import ttk
from component.menubar import Menubar
from component.tabControl import TabControl
from component.tabContainer import TabContainer

from utility.weatherUtil import GetWeatherApp

class Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python GUI")
        self.resizable(1,1)
        self.geometry('450x250')
        self.configUI()

    def configUI(self):
        self.config(menu=Menubar(self))
        self.tabControl = TabControl(self, width=400, height=200)
        self.tabContainer = TabContainer(self)

def main():
    root = Win()
    weatherApp = GetWeatherApp(root.tabContainer.mainTabContainer)
    root.mainloop()

if __name__ == '__main__':
    main()
