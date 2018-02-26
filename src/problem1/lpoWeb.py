from datetime import date
from urllib import request

BASE_URL = 'http://lpo.dt.navy.mil/data/DM'

def get_data_for_date(date):
    """
    # Returns an generator object of data for the specified date.
    Output data is formatted as a dict.
    """

    if date.year < 2007:
        return _get_data_pre2007(date)
    else:
        return _get_data_post2006(date)

def _get_data_pre2007(date):
    """
    # Access the LPO website to retrieve data for the specified date.
    For dates from 2002 to 2006, data is downloaded for the full year.
    The method operates as a generator object containing dictionaries
    with result data.
    """

    ### 1 - this builds the url based on year.
    url = '{}/Environmental_Data_{}.txt'.format(BASE_URL, date.year)
    print('Fetching online data for {} (full year)'.format(date.year))

    try:
        year_data = request.urlopen(url).read().decode(encoding='utf_8').split('\n')
    except:
        raise ValueError(date) # raise error accessing website.
    else:
        year_data.pop(0) # remove first item which contains column header info.

    for line in year_data:
        elements = line.split()
        yield dict(Date = elements[0], Time = elements[1], Status = 'COMPLETE', Air_Temp = elements[5], Barometric_Press = elements[7], Wind_Speed = elements[2])

def _get_data_post2006(date):
    url = '{}/{}/{}/'.format(BASE_URL, date.year, str(date).replace('-','_'))
    data = dict(Air_Temp = [], Barometric_Press = [], Wind_Speed = [])
    print('Fetching online data for {}'.format(data))
    for key in data.keys():
        try:
            data[key] = request.urlopen('{}{}'.format(url, key)).read().decode(encoding='utf_8').split('\r\n')
        except Exception as e:
            raise
        else:
            pass
    return None

def _test():
    pass

if __name__ == '__main__':
    _test()
