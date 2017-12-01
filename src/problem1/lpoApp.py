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
        # init constructor method to handle initialisations for objects/variables and GUI method
        pass

    def _createGUI(self):
        # method to build the user interface
        pass

    def _submit_callback(self):
        # method to handle a submit Button
        pass

    def _safe_close(self):
        # method to handle everything to be shut down properly (exit)
        pass

def main():

    root = Tk() # to create a new top-level window for the GUI and store it in a variable (object)
    app = lpoApp(root) # root (object) is passed to the lpoApp constructor
    root.mainloop() # mainloop() gets invoked so that the GUI enters into the tk event loop

if __name__ == '__main__':
    main()
