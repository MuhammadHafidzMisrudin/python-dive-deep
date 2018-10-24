def isLeapYearOne(year):
    lear_year = True
    if (year % 4 == 0):
        return lear_year
    if (year % 100 == 0):
        lear_year =  False
    if (year % 400 == 0):
        return lear_year
    else:
        lear_year = False

    return lear_year

################################################################################

def isLeapYearTwo(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print('{0} is a leap year'.format(year))
            else:
                print('{0} IS NOT a leap year'.format(year))
        else:
            print('{0} is a leap year'.format(year))
    else:
        print('{0} IS NOT a leap year'.format(year))

################################################################################

def isLeapYearThree(year):
    return ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))

################################################################################

def isLeapYearFour(year):
    if (year % 4 != 0):
        print('{0} IS NOT a leap year'.format(year))
    elif (year % 100 != 0):
        print('{0} is a leap year'.format(year))
    elif (year % 400 != 0):
        print('{0} IS NOT a leap year'.format(year))
    else:
        print('{0} is a leap year'.format(year))


################################################################################

print(isLeapYearOne(2000))
print(isLeapYearOne(2001))
print(isLeapYearOne(2004))
print(isLeapYearOne(2017))
print('\n')
print(isLeapYearTwo(2000))
print(isLeapYearTwo(2001))
print(isLeapYearTwo(2004))
print(isLeapYearTwo(2017))
print('\n')
print(isLeapYearThree(2000))
print(isLeapYearThree(2001))
print(isLeapYearThree(2004))
print(isLeapYearThree(2017))
print('\n')
print(isLeapYearFour(2000))
print(isLeapYearFour(2001))
print(isLeapYearFour(2004))
print(isLeapYearFour(2017))
