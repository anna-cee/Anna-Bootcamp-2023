import time
import datetime
from datetime import timedelta


def ten_sec_guess():
    start = input("press enter to start")
    start = datetime.datetime.now()
    end = input('Press enter when ten secs is up')
    end = datetime.datetime.now()
    guess = (end - start).total_seconds()
    #start_delta = int(datetime.timedelta(seconds=start.second))
    #end_delta = int(datetime.timedelta(seconds=end.second))
    #guess = int(end_delta) - int(start_delta)
    #return timedelta(seconds=start-end)

    print(guess)

#strftime("%H:%M:%S")
# import time

# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)

(ten_sec_guess())

   
# Tell them to hit enter key when ready

# Get the first time in seconds

# Get them to hit the enter key when they think 10 seconds have passed

# Get the second time in seconds

# Subtract first time from the second time

# Tell them how close to 10 the answer was.
