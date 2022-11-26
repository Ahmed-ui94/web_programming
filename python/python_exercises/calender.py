import calendar

year = int(input("Enter the year: (1901 to 2099): ") )
month = int(input("choose a month from: "))
day = input("choose a day from that month: ")

#mon = calendar.TextCalendar()
#cal = fmon.formatmonth(year, month, w=3)

#print(cal.replace('\n','\n').replace(''+day,'*'+day, 1))

def calenderformater():
    fmon = calendar.TextCalendar()
    cal = fmon.formatmonth(year, month, w=3)

    return cal.replace('\n','\n').replace(''+day,'*'+day, 1)

print(calenderformater())