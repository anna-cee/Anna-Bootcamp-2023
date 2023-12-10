#import datetime
#import calendar 


import datetime

x = datetime.datetime.now()
x = datetime.date

print(x.year)
print(x.strftime("%A"))


#     Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

import datetime
import calendar 
def birthday_weekday():
    m = int(input("Please enter your birth month.."))
    d = int(input("Please enter your birth date of the month e.g. 19 ..."))
    birthday = datetime.datetime(2023, m, d)
    print(birthday.strftime("%A")) #date = str(f'1-',y)
    #print(birthday)



(birthday_weekday())
#print (datetime.date)
# Prompt a user to enter the month and day of their birthday, and print what day of
# the week their birthday falls on this year.

#datetime.date()

# calendar.weekday(year, month, day)

#     Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

#THIS SOLUTION WAS MARKED CORRECT IN ED
import datetime
import calendar 
def birthday_weekday():
    m = int(input("Enter the month: "))
    d = int(input("Enter the day: "))
    birthday = datetime.datetime(2023, m, d)
    weekday = birthday.strftime("%A")
    print(f"Your birthday falls on a {weekday} in 2023!") 
   

(birthday_weekday())