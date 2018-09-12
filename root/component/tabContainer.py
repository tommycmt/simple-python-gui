from tkinter import ttk

class TabContainer():
    def __init__(self, win, *args, **kwargs):
        for module in kwargs['module']:
            func = mapping[module]
            setattr(self, module, func(getattr(win.tabControl, module), text=module.capitalize()))

class MainTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)
        
class WeatherTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)
        
class WarframeTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)

mapping = {'main': MainTabContainer,
           'weather': WeatherTabContainer,
           'warframe': WarframeTabContainer}
