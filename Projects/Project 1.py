#Project 1: Water Reminder
#Name: Bradley Davidson
#Date: 2/21/21

from win10toast import ToastNotifier
import threading
import time

toaster = ToastNotifier() #notification library
def water_timer(interval):
    try: # The try/catch block in this case is used to break out of the while loop
        while True:
            #sleep first so that the first reminder is x amount of time after starting rather than right away
            time.sleep(interval)
            toaster.show_toast("Water Reminder", "Take a drink of water!", duration = 10)
    except KeyboardInterrupt:
        #program is canceled
        print('Water Reminder canceled')

reminder_interval = int(input("How often (in minutes) would you like to be reminded to drink water? "))
reminder_interval = reminder_interval * 60 # converts minutes to seconds to be usable by time.sleep()
print("""Reminder Set!
To stop these reminders, press ctrl + C""")
water_timer(reminder_interval)

###### References
### Link: https://stackoverflow.com/questions/18994912/ending-an-infinite-while-loop
### I used this method described by Steve Howard for canceling the infinite loop

### Link: https://pypi.org/project/win10toast/
### documentation for the ToastNotifier library


