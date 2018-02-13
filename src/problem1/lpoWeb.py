from datetime import date
from urllib import request

BASE_URL = 'http://lpo.dt.navy.mil/data/DM'

def get_data_for_date(date):
    if date.year < 2007:
        return None
    else:
        return None

def _get_data_pre2007(date):
    pass

def _get_data_post2006(date):
    pass

def _test():
    pass

if __name__ == '__main__':
    _test()
