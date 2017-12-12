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

        self.master = master # stores the Tkinter top-level window object as an internal object called, master
        self._createGUI() # initialises and invokes the GUI handler
        self.database = lpoDB.lpoDB() # creates and stores a new database object from the lpoDB module
        self.master.protocol("WM_DELETE_WINDOW", self._safe_close) # configures master window to capture the event the user closes the application to execute _safe_close method

    def _createGUI(self):
        # method to build the user interface
        ### 1 - configures style of the GUI
        bgcolor = '#CCCCFF'
        self.master.configure(background = bgcolor) # property window background color
        self.master.title('Lake Pend Oreille')
        self.master.resizable(False, False) # property for resizable window

        self.style = ttk.Style() # creates  a tkinter (ttk) style object to configure the background color and font attributes
        self.style.configure('TFrame', background = bgcolor) # configures background color for frame
        self.style.configure('TButton', background = bgcolor, font = ('Arial Black', 10)) # configures background color for button
        self.style.configure('TLabel', background = bgcolor, font = ('Arial Black', 10)) # configures background color for label
        self.style.configure('Status.TLabel1', background = bgcolor, font = ('Arial', 10))
        self.style.configure('Result.TLabel1', background = bgcolor, font = ('Courier', 10))

        # create a tk frame widget
        ### 2 - create and display header frame with image
        self.frame_header = ttk.Frame(self.master) # create a tkinter frame header object to hold the header image
        self.frame_header.pack(side = TOP) # place the header image at the top of the window
        self.logo = PhotoImage(file = 'lpo_logo.gif') # create a photo image object (xxx.gif) using PhotoImage()
        ttk.Label(self.frame_header, image = self.logo).pack() # display it using label inside of the header frame

        # create a frame to store the input control
        ### 3 - create and display frame to hold user input widgets
        self.frame_input = ttk.Frame(self.master) # create the input frame to display the start and end dates
        self.frame_input.pack(side = TOP)

        # diplay text string for start and end dates using tk Label widgets inside of the frame
        ttk.Label(self.frame_input, text = 'Start Date:').grid(row = 0, column = 1, columnspan = 3, sticky = 'sw')
        ttk.Label(self.frame_input, text = 'End Date:').grid(row = 0, column = 5, columnspan = 3, sticky = 'sw')

        # create tkinter string variables for the day, month and year for both the start and end dates
        # which to store the input values of the start and end dates
        self.start_day = StringVar()
        self.start_month = StringVar()
        self.start_year = StringVar()
        self.end_day = StringVar()
        self.end_month = StringVar()
        self.end_year = StringVar()

        # create a list of strings that contains each value of the 12 months for user input for spinbox widgets.
        self.months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

        # create individual Spinboxes widgets for the user to input values which are tied to each of those tkinter string variables (objects)
        ### 4 - create a Spinbox for each day, month, year of the start and end dates
        Spinbox(self.frame_input, from_ = 1, to = 31, textvariable = self.start_day, width = 2, font = 'Courier 12').grid(row = 1, column = 1)
        Spinbox(self.frame_input, values = self.months, textvariable = self.start_month, width = 3, font = 'Courier 12').grid(row = 1, column = 2)
        Spinbox(self.frame_input, from_ = 2007, to = date.today().year, textvariable = self.start_year, width = 4, font = 'Courier 12').grid(row = 1, column = 3)
        Spinbox(self.frame_input, from_ = 1, to = 31, textvariable = self.end_day, width = 2, font = 'Courier 12').grid(row = 1, column = 5)
        Spinbox(self.frame_input, values = self.months, textvariable = self.end_month, width = 3, font = 'Courier 12').grid(row = 1, column = 6)
        Spinbox(self.frame_input, from_ = 2007, to = date.today().year, textvariable = self.end_year, width = 4, font = 'Courier 12').grid(row = 1, column = 7)

        # after creating the Spinboxes, set their default values to represent the current date,
        # retrieve dates using the today method from the datetime module
        ### 5 - set default values (for Spinboxes widgets) for the start and end dates to today
        self.start_day.set(date.today().day)
        self.start_month.set(self.months[date.today().month-1])
        self.start_year.set(date.today().year)
        self.end_day.set(date.today().day)
        self.end_month.set(self.months[date.today().month-1])
        self.end_year.set(date.today().year)

        ### 6 - create these Labels (using the tkinter grid geometry manager) for padding purposes
        # add few extra labels to help space things out for Spinboxes widgets
        ttk.Label(self.frame_input).grid(row = 1, column = 0, padx = 5)
        ttk.Label(self.frame_input).grid(row = 1, column = 4, padx = 5)
        ttk.Label(self.frame_input).grid(row = 1, column = 8, padx = 5)
        #ttk.Label(self.frame_input).grid(row = 1, column = 4, padx = 5)
        #ttk.Label(self.frame_input).grid(row = 1, column = 8, padx = 5)

        ### 7 - create the submit button
        # The command property of the Submit button is configured to execute the submit_callback() whenever the button event is triggered
        ttk.Button(self.frame_input, text = 'Submit', command = self._submit_callback).grid(row = 2, column = 0, columnspan = 9, pady = 5)

        ### 8 - create a frame to display results, but do not show it yet
        # a frame to hold the results and populates it with the appropriate Labels.
        self.frame_result = ttk.Frame(self.master)

        ttk.Label(self.frame_result, text = 'Mean:').grid(row = 1, column = 0, padx = 5)
        ttk.Label(self.frame_result, text = 'Median:').grid(row = 2, column = 0, padx = 5)

    def _submit_callback(self):
        # method to handle a submit Button
        pass

    def _safe_close(self):
        '''
        # method to handle everything to be shut down properly (exit), when user closes the application window
          note: This is called when the user closes the GUI. It ensures the database is properly shut down first
        '''
        self.database.close()
        self.master.destroy()

def main():

    root = Tk() # to create a new top-level window for the GUI and store it in a variable (object)
    app = lpoApp(root) # root (object) is passed to the lpoApp constructor
    root.mainloop() # mainloop() gets invoked so that the GUI enters into the tk event loop

if __name__ == '__main__':
    main()
