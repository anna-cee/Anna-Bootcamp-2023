import datetime
import calendar 

def agedays():
    y = int(input('Enter birth year:'))
    m = int(input('Enter month: '))
    d = int(input('Enter day: '))
    dob =(datetime.date(y, m, d))
    today = datetime.date.today()
    liveddays = today - dob
    print(liveddays)
   
   #print(dob)
    #print(datetime.date.today())

    

agedays()



# Write a program to work out how many days you have lived for. 

# Enter date of birth

# Get today’s date

# Get the difference in days between the two dates

# Display result 