from tkinter import ttk

class TabContainer():
    def __init__(self, win, *args, **kwargs):
        for module in kwargs['module']:
            func = mapping[module]
            setattr(self, module, func(getattr(win.tabControl, module)))

class MainTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)
        self.text = "Main"
        
class WeatherTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)
        self.text = "Weather"
        
class WarframeTabContainer(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(column=0, row=0, padx=8, pady=4)
        self.text = "Warframe"

mapping = {'main': MainTabContainer,
           'weather': WeatherTabContainer,
           'warframe': WarframeTabContainer}
