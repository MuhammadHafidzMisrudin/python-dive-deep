#!/usr/bin/python3
# lpoApp.py by Muhammad Hafidz
# App module python file the Lake Pend Oreille

from tkinter import *
from tkinter import ttk, messagebox
from statistics import mean, median
from datetime import date
import lpoDB


class lpoApp:


def main():

    root = Tk()
    app = lpoApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
