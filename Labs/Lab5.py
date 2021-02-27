import datetime

#Assignment: Lab 5
#Name: Bradley Davidson
#Date: 2/14/2021

#prompt: Take a birthday date input and calculate how many seconds old you are 

birthday = input('When is your birthday? (mm/dd/yyyy) ')
month, day, year = map(int, birthday.split('/')) #parses the string input into a usable format for timespan
birthday_date = datetime.datetime(year, month, day, 0) #creates a datetime object with time set to midnight
today_date = datetime.datetime.now() #gets current date and time
timespan = today_date - birthday_date #creates a time delta object
print("You have been alive for " + str(int(timespan.total_seconds())) + " seconds, wow!") # for our purposes, I don't really care about micro seconds. I casted to int to easily chop off decimal point