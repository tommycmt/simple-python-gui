from tkinter import ttk

class TabControl(ttk.Notebook):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.mainTab = MainTab(self)
        self.functionTab = FunctionTab(self)
        self.add(self.mainTab, text="Weather")
        self.add(self.functionTab, text="A")
        self.pack(expand=1, fill="both")

class MainTab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
class FunctionTab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

