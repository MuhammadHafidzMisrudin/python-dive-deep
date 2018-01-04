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
        # method to build the graphical user interface
        ### 1 - configures style of the GUI
        bgcolor = '#CCCCFF'
        self.master.configure(background = bgcolor) # property window background color
        self.master.title('Lake Pend Oreille')
        self.master.resizable(False, False) # property for resizable window

        self.style = ttk.Style() # creates  a tkinter (ttk) style object to configure the background color and font attributes
        self.style.configure('TFrame', background = bgcolor) # configures background color for frame
        self.style.configure('TButton', background = bgcolor, font = ('Arial Black', 10)) # configures background color for button
        self.style.configure('TLabel', background = bgcolor, font = ('Arial Black', 10)) # configures background color for label
        self.style.configure('Status.TLabel', background = bgcolor, font = ('Arial', 10))
        self.style.configure('Result.TLabel', background = bgcolor, font = ('Courier', 10))

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

        # create a list (tuple) of strings that contains each value of the 12 months for user input for spinbox widgets.
        self.months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

        # create individual Spinboxes widgets for the user to input values which are tied to each of those tkinter string variables (objects)
        ### 4 - create a Spinbox for each day, month, year of the start and end dates
        Spinbox(self.frame_input, from_ = 1, to = 31, textvariable = self.start_day, width = 2, font = 'Courier 12').grid(row = 1, column = 1)
        Spinbox(self.frame_input, values = self.months, textvariable = self.start_month, width = 3, font = 'Courier 12').grid(row = 1, column = 2)
        Spinbox(self.frame_input, from_ = 2009, to = date.today().year, textvariable = self.start_year, width = 4, font = 'Courier 12').grid(row = 1, column = 3)
        Spinbox(self.frame_input, from_ = 1, to = 31, textvariable = self.end_day, width = 2, font = 'Courier 12').grid(row = 1, column = 5)
        Spinbox(self.frame_input, values = self.months, textvariable = self.end_month, width = 3, font = 'Courier 12').grid(row = 1, column = 6)
        Spinbox(self.frame_input, from_ = 2009, to = date.today().year, textvariable = self.end_year, width = 4, font = 'Courier 12').grid(row = 1, column = 7)

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
        # it doesn't make it visible for the user to see the results frame unless there are valid results to display to them
        self.frame_result = ttk.Frame(self.master)

        # 5 Labels are static and simply identify and the rows and columns of the result table
        # create Label widgets for the Mean and Median results
        ttk.Label(self.frame_result, text = 'Mean:').grid(row = 1, column = 0, padx = 5)
        ttk.Label(self.frame_result, text = 'Median:').grid(row = 2, column = 0, padx = 5)

        # create Label widgets for the Air Temperature, Barometric Pressure, Wind Speed results
        ttk.Label(self.frame_result, text = 'Air\nTemp:', justify = CENTER).grid(row = 0, column = 2, sticky = 'e', padx = 5)
        ttk.Label(self.frame_result, text = 'Barometric\nPressure:', justify = CENTER).grid(row = 0, column = 3, sticky = 'e', padx = 5)
        ttk.Label(self.frame_result, text = 'Wind\nSpeed:', justify = CENTER).grid(row = 0, column = 1, sticky = 'e', padx = 5)

        ### 9 - create tkinter string variables for each of the six types of weather statistics
        self.air_temp_mean = StringVar()
        self.air_temp_median = StringVar()
        self.barometric_press_mean = StringVar()
        self.barometric_press_median = StringVar()
        self.wind_speed_mean = StringVar()
        self.wind_speed_median = StringVar()

        ### 10 - create 6 Label widgets which are each tied to initialised individual string variables (objects) using the textvariable property
        # When the results are stored into string variables, the Labels will be automatically updated to display them
        ttk.Label(self.frame_result, textvariable = self.air_temp_mean, style = 'Result.TLabel').grid(row = 1, column = 2)
        ttk.Label(self.frame_result, textvariable = self.air_temp_median, style = 'Result.TLabel').grid(row = 2, column = 2)
        ttk.Label(self.frame_result, textvariable = self.barometric_press_mean, style = 'Result.TLabel').grid(row = 1, column = 3)
        ttk.Label(self.frame_result, textvariable = self.barometric_press_median, style = 'Result.TLabel').grid(row = 2, column = 3)
        ttk.Label(self.frame_result, textvariable = self.wind_speed_mean, style = 'Result.TLabel').grid(row = 1, column = 1)
        ttk.Label(self.frame_result, textvariable = self.wind_speed_median, style = 'Result.TLabel').grid(row = 2, column = 1)


    def _submit_callback(self):
        # method to handle a submit Button.

        ### 1 - check that the input values are a real, legitimate date.
        # it retrieves the values for day, month and year from the Spinboxes (widgets),
        # then it attempts to interpret and convert those values into a datetime object using the date method.
        # implement try..except statement for handling exception for valid input values,
        # because if the user inputs values which do not represent an actual date, then the date method will throw a value error exception.
        try:
            start = date(int(self.start_year.get()), self.months.index(self.start_month.get()) + 1, int(self.start_day.get())) # format: date(Y, M, D)
            end = date(int(self.end_year.get()), self.months.index(self.end_month.get()) + 1, int(self.end_day.get())) # format: date(Y, M, D)
        except ValueError as e:
            # display a pop-up (error) message due to invalid date.
            messagebox.showerror(title = 'ValueError', message = ('INVALID DATE\n Correct format is "DD Mon YYYY"'))

            # reset default start and end dates to today.
            # reset the date to the current dates, then return out of the submit_callback method.
            self.start_day.set(date.today().day)
            self.start_month.set(self.months[date.today().month-1])
            self.start_year.set(date.today().year)
            self.end_day.set(date.today().day)
            self.end_month.set(self.months[date.today().month-1])
            self.end_year.set(date.today().year)
            return

        ### 2 - check that date range is valid.
        # it does some range checking on the input dates.
        # the online database (start) date begins on the 10th of January 2010, if the user inputs a start date before that,
        # or an end date after that (current date) or, if a start date is after the end date, it will display an error message to the user and return out of the submit_callback().
        if (start < date(2010, 1, 10)) or (end > date.today()) or (start > end):
            messagebox.showerror(title = 'ValueError', message = ('INVALID DATE RANGE\nStart Date: {}\nEnd Date: {}\nDate must be between 2010-10-1 and {}.\n Start Date must be <= End Date').format(start, end, date.today()))
            return

        ### 3 - initialise a list of data (to extract data from the online database).
        # after it verifies the input dates are both valid in format in range, next line is to retrieve the weather data to calculate statistics for the requested dates.
        # get_data_for_range() gets invoked from lpo database module (lpoDB.py) which returns a generator object with a dictionary containing each of the 3 types of weather data,
        # for the database entry in the requested range of dates.
        # convert the generator object into a list and store it in an object variable called "data".
        data = list(self.database.get_data_for_range(start, end))

        ### 4 - check to make sure that the application is able to retrieve data from the database.
        if data != []:

            ### 5 - the lists will hold all values from the date range for each weather parameter (statistics).
            # create a dictionary with 3 (empty) lists, one for each weather parameter (each type).
            # then append the retrieved data to the appropriate lists, so each list will contain all of the data values for the weather parameter,
            # it represents over the entire requested range of dates.
            # these lists will be used to feed the mean and median statistics functions.
            dict_of_lists = dict(Air_Temp = [], Barometric_Press = [], Wind_Speed = [])

            ### 6 - implement for loop cycles through each of entries in the data list  which represent dictionaries of values for individual database entries.
            # it indexes out each of the weather data types  using the "key" names, and then it appends the values to the appropriate lists for my dictionary of lists.
            for entry in data:
                for key in dict_of_lists.keys():
                    dict_of_lists[key].append(entry[key])

            ### 7 - calculate the mean & median for each type of data; store results of statistics calculation in dictionaries (of lists).
            # create a blank dictionary to hold the statistical results for each weather parameter.
            # the for loop uses the keys method, .keys() to cycle through each of the elements in the dictionary of lists,
            # calculates the mean and median for each each list using functions from the statistics module.
            # those collective (mean and median) values are packed into a dictionary which it then stores in the results dictionary.
            # result (variable) - dictionary of dictionaries.
            result = {}
            for key in dict_of_lists.keys():
                result[key] = dict(mean = mean(dict_of_lists[key]), median = median(dict_of_lists[key]))

            ### 8 - set StringVar (individual string variable that are initialised in _createGUI()) associated with the results labels (widgets)
            # store the results into their respected string variables by using the set method, .set()
            self.air_temp_mean.set('{0:.2f}'.format(result['Air_Temp']['mean']))
            self.air_temp_median.set('{0:.2f}'.format(result['Air_Temp']['median']))
            self.barometric_press_mean.set('{0:.2f}'.format(result['Barometric_Press']['mean']))
            self.barometric_press_median.set('{0:.2f}'.format(result['Barometric_Press']['median']))
            self.wind_speed_mean.set('{0:.2f}'.format(result['Wind_Speed']['mean']))
            self.wind_speed_median.set('{0:.2f}'.format(result['Wind_Speed']['mean']))

            ### 9 - display the results frame
            self.frame_result.pack(side = TOP)
        else:
            self.frame_result.forget()

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
