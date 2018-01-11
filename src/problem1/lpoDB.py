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
        pass

    def _get_status_for_range(self, start. end):
        pass

    def _update_data_for_date(self, date, partial):
        pass

    def clear(self):
        pass

    def close(self):
        pass

def test():
    pass
