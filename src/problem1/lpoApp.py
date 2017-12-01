#!/usr/bin/python3
# lpoApp.py by Muhammad Hafidz
# App module python file the Lake Pend Oreille

from tkinter import *
from tkinter import ttk, messagebox
from statistics import mean, median
from datetime import date
import lpoDB


class lpoApp:

    def __init__(self, master):
        pass

    def _createGUI(self):
        pass

    def _submit_callback(self):
        pass

    def _safe_close(self):
        pass

def main():

    root = Tk() # to create a new top-level window for the GUI and store it in a variable (object)
    app = lpoApp(root) # root (object) is passed to the lpoApp constructor
    root.mainloop() # mainloop() gets invoked so that the GUI enters into the tk event loop

if __name__ == '__main__':
    main()
