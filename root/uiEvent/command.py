import sys
from tkinter import messagebox as mBox

global isStopped

def _quit(root):
    with root.configs.condition:
        root.configs.isStopped = True
        root.configs.condition.notify_all()
    root.quit()
    root.destroy()

def _about():
    mBox.showinfo('About', 'Copyright © 2018 Tommy Tang\nAll Rights Reserved！')
