def isBigMonth(month):
    bigMonth = [1,3,5,7,8,10,12]
    if (month in bigMonth):
        return True
    else:
        return False
        
def isLeapYear(year):
    if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False

def validateDate(year1, month1, day1, year2, month2, day2):
    if(year1 < year2):
        return True
    elif(year1 == year2):
        if(month1 < month2):
            return True
        elif(month1 == month2):
            if(day1 < day2):
                return True
    else:
        return False
            

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    yearCount = year1
    monthCount = month1
    dayCount = day1
    
    while(validateDate(yearCount, monthCount, dayCount, year2, month2, day2)):
        days += 1
        if(monthCount == 12 and dayCount == 31):
            monthCount = 1
            dayCount = 0
            yearCount += 1
        if(isLeapYear(yearCount) and monthCount == 2):           #is month 2 in a leap year
            if(dayCount == 29):
                dayCount = 1
                monthCount += 1
            else:
                dayCount += 1

        elif(isLeapYear(yearCount) != True and monthCount == 2): #is month 2 not leap year
            if(dayCount == 28):
                dayCount = 1
                monthCount += 1
            else:
                dayCount += 1

        elif(monthCount != 2):         #not month 2(does not matter if its leap year)
            if(isBigMonth(monthCount)):                          #Its a big month
                if(dayCount == 31):                              #Is the 31st day of the month
                    dayCount = 1
                    monthCount += 1
                else:                                            #Is not the 31st day of the month
                    dayCount += 1
            elif(isBigMonth(monthCount) == False):               #Its not a big month
                if(dayCount == 30):
                    dayCount = 1
                    monthCount += 1
                else:
                    dayCount += 1
       # print days, yearCount, monthCount, dayCount
    return days

print daysBetweenDates(1900,1,1,1999,12,31)



