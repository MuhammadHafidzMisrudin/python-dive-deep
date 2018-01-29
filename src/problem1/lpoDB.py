#!/usr/bin/python3
# lpoDB.py by Muhammad Hafidz

from datetime import date, datetime, timedelta
from tkinter import messagebox
import sqlite3
import lpoWeb

class lpoDB():
    '''
    # A database module class to keep of Wind Speed, Air Temperature, and Barometric Pressure for specific dates.
    # The module's functionalities:
      - Open/create database and configure table with the appropriate columns.
      - Determine which dates have complete/incomplete data available in the database.
      - Use lpoWeb module to download incomplete data from online API (navy.mil).
      - Cache downloaded data into the database for future use.
      - Return data for all requested range of dates to the lpoApp module.
    '''

    def __init__(self, **kwargs):
        # kwargs - keyword arguments (the caller can use to specify the name of the database file and the name of the table).
        self.filename = kwargs.get('filename', 'lpo.db') # class variable with default values.
        self.table = kwargs.get('table', 'Weather') # class variable with default values.

        self.db = sqlite3.connect(self.filename) # sqlite3.connect() method is called to open the database.
        self.db.row_factory = sqlite3.Row # the "Row" method to configure the row_factory for retrieving data.
        self.db.execute('''CREATE TABLE IF NOT EXISTS {} (Date TEXT, Time TEXT, Status TEXT, Air_Temp FLOAT, Barometric_Press FLOAT, Wind_Speed FLOAT)'''.format(self.table))

    def __iter__(self):
        '''
        # This method is to return generator object with dictionaries (dicts) of entire DB contents.
        '''
        cursor = self.db.execute('SELECT * FROM {} ORDER BY  Date, Time'.format(self.table))
        for row in cursor:
            yield dict(row)

    def get_data_for_range(self, start, end):
        '''
        # Given a start and end date, method to return a generator of dicts (dictionaries),
        containing all available Air_Temp, Barometric_Press, and Wind_Speed.
        NOTE - It updates the database as necessary first.
        '''

        dates_to_update = [] # create a list for dates.

        ### 1 - determine pre-2007 dates to update and append to list.
        for year in range(start.year, 2007):
            if list(self._get_status_for_range(date(year, 1, 12), date(year, 1, 12))) == []:
                dates_to_update.append(date(year, 1, 12)) # format: date(Year, Month, Day).

        ### 2 - determine post-2006 dates to update and append to list.
        if (end.year > 2006) and (start >= date(2007, 1, 1)):
            temp_start = start
        elif (end.year > 2006) and (start < date(2007, 1, 1)):
            temp_start = date(2007, 1, 1)
        else:
            # otherwise, start and end dates are both pre-2007.
            temp_start = end

        ### 3 - generate a list of dates between temp_start and end.
        delta = end - temp_start # create a variable, delta.
        for d in range(delta.days + 1):
            # note: the +1 makes it inclusive.
            dates_to_update(temp_start + timedelta(days = d))

        statuses = list(self._get_status_for_range(temp_start, end))

        ### 4 - remove all dates from dates_to_update that have a 'COMPLETE' or 'PARTIAL' status.
        for entry in statuses:
            if entry['Status'] ==  'COMPLETE':
                dates_to_update.remove(datetime.strptime(str(entry['Date']), '%Y%m%d').date())
            elif entry['Status'] == 'PARTIAL':
                try:
                    # update for any new data first, then remove from dates_to_update list.
                    self._update_data_for_date(datetime.strptime(str(entry['Date']), '%Y%m%d').date(), True)
                except:
                    raise dates_to_update.remove(datetime.strptime(str(entry['Date']), '%Y%m%d').date(), True)

        ### 5 - iterate through dates that were non-existent in DB and insert data.
        error_dates = []
        for day in dates_to_update:
            try:
                self._update_data_for_date(day, False)
            except ValueError as e:
                error_dates.append(e)

        if error_dates != []:
            error_message = 'There were problems accessing data for the following dates.  They were not included in the result.\n'
            for day in error_dates:
                error_message += '\n{}'.format(day)
            messagebox.showwarning(title = 'Warning', message = error_message)

        ### 6 - get Air_Temp, Barometric_Press, and Wind_Speed data from start/end dates range in database.
        cursor =  self.db.execute('''SELECT Air_Temp, Barometric_Press, Wind_Speed FROM {} WHERE Date BETWEEN {} AND {}'''.format(self.table, start.strftime('%Y%m%d'), end.strftime('%Y%m%d')))

        for row in cursor:
            yield dict(row)
        #return None

    def _get_status_for_range(self, start, end):
        cursor = self.db.execute('''SELECT DISTINCT Date, Status FROM {} WHERE Date BETWEEN {} AND {}'''.format(self.table, start.strftime('%Y%m%d'), end.strftime('%Y%m%d')))

        for row in cursor:
            yield dict(row)
        return None

    def _update_data_for_date(self, date, partial):
        pass

    def clear(self):
        pass

    def close(self):
        pass

def test():
    pass
