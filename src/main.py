import os
import sys

from tkinter import Tk

path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, path)

from app.gui.main_screen import MainHTR

if __name__ == '__main__':
    window = Tk()
    app = MainHTR(window)
    window.resizable(False, False)
    window.mainloop()