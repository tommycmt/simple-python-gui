from tkinter import ttk

class TabControl(ttk.Notebook):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        for module in kwargs['module']:
            func = mapping[module]
            setattr(self, module, func(self))
        self.pack(expand=1, fill="both")

class MainTab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        parent.add(self, text="Main")
        
class WeatherTab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        parent.add(self, text="Weather")

class WarframeTab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        parent.add(self, text="Warframe")

mapping = {'main': MainTab,
           'weather': WeatherTab,
           'warframe': WarframeTab}
