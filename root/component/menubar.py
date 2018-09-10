import tkinter as tk
from functools import partial
from uiEvent import command as command

class Menubar(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.file_menu = FileMenu(self, tearoff=0)
        self.edit_menu = EditMenu(self, tearoff=0)
        self.add_cascade(label="File", menu=self.file_menu)
        self.add_cascade(label="Edit", menu=self.edit_menu)

class FileMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.add_command(label="Quit", command=partial(command._quit,parent))

class EditMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.add_command(label="About", command=command._about)
