from tkinter import ttk

class TabContainer():
    def __init__(self, win):
        self.mainTabContainer = MainTabContainer(win.tabControl.mainTab, text='Main')
        self.functionTabContainer = FunctionTabContainer(win.tabControl.functionTab, text='Function')

class MainTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)

class FunctionTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)
