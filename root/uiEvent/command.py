from tkinter import messagebox as mBox

def _quit(win):
    win.quit()
    win.destroy()
    exit()

def _about():
    mBox.showinfo('About', 'Copyright © 2018 Tommy Tang\nAll Rights Reserved！')
