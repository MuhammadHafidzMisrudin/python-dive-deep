from datetime import date
from urllib import request

BASE_URL = 'http://lpo.dt.navy.mil/data/DM'

def get_data_for_date(date):
    """
    Returns an generator object of data for the specified date.
    Output data is formatted as a dict.
    """

    if date.year < 2007:
        return _get_data_pre2007(date)
    else:
        return _get_data_post2006(date)

def _get_data_pre2007(date):
    url = '{}/Environmental_Data_{}.txt'.format(BASE_URL, date.year)
    print('Fetching online data for {} (full year)'.format(date.year))

    try:
        year_data = request.urlopen(url).read().decode(encoding='utf_8').split('\n')
    except:
        raise ValueError(date)
    else:
        year_data.pop(0)
    pass

def _get_data_post2006(date):
    pass

def _test():
    pass

if __name__ == '__main__':
    _test()
