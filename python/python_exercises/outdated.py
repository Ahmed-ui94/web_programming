from re import *

Months = [
    'January',
    "February",
    "April",
    "May",
    "June",
    "July",
    "August",
    "Septemper",
    "October",
    "November",
    "December"
]

    
while True:
    date = input("date: ")
    try:
        # split the date by /
        month, day, year = date.split("/")
        #check if month is in between 1 and 12 and day between 1 and 31
        if (12 >= int(month) >= 1) and (31 >= int(day) >=1):

            break 
                          
    except :
        #split date by space
        name_month, day1, year = date.split(" ")
        # find the number of the month
        for i in range(len(Months)):
            if name_month == Months[i]:
                month = i + 1
                break
        #remove comma from day variable
        day = day1.replace(",", "")
        #check if month is in between 1 and 12 and day between 1 and 31
        if (12 >= month >= 1) and (31 >= int(day) >=1):
            break
        else:
            print()
            pass
#if month is less  than 10, add a 0 before
# if day is less than 10, add a 0 before
#print the result
       
print(f'{year}-{int(mont):02}-{int(day):02}')
