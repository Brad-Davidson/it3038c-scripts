import speech_recognition as sr 
import wikipedia
import warnings
from win10toast import ToastNotifier
import threading
import time

toaster = ToastNotifier() #notification library

warnings.catch_warnings()
warnings.simplefilter("ignore") #This is to ignore a warning thrown by the wikipedia library, as other errors are being manually caught

recognizer = sr.Recognizer()
mic = sr.Microphone()

def water_timer(interval):
    while True:
         #sleep first so that the first reminder is x amount of time after starting rather than right away
        time.sleep(interval)
        toaster.show_toast("Water Reminder", "Take a drink of water!", duration = 10)
def stretch_timer(interval):
    while True:
        time.sleep(interval)
        toaster.show_toast("Stretch Reminder", "Get up and stretch for a bit!", duration = 30)
        time.sleep(30) #stretch for 30 seconds
        toaster.show_toast("Stretch Reminder", "You can get back to work!", duration = 10)
def display_summary(term):
    try:
        print("====== Results for " + term + " ======")
        print("")
        print(wikipedia.summary(term))
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous term, select one of the terms below:")
        print(e.options)
    except wikipedia.exceptions.PageError as e:
        print("Page not able to be retrieved.")

def monitor_speech():
    while True:

        with mic as source:
            #tune the recognizer to adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            #listen to the mic input
            audio = recognizer.listen(source)
        try:
            result = recognizer.recognize_google(audio) #use google libraries to read the audio
            if len(result.split(' ')) > 0 and result.split(' ')[0] == "Wikipedia": #if the phrase starts with "Wikipedia"
                print("Searching for " + result.split(' ', 1)[1])
                display_summary(result.split(' ', 1)[1]) #display the results of Wikipedia.summary(<terms after the wikipedia phrase word")
        except:
            print("Couldn't understand audio")

#Main code
def main():
    water_reminder_interval = int(input("How often (in minutes) would you like to be reminded to drink water? "))
    stretch_reminder_interval = int(input("How often (in minutes) would you like to be reminded to get up and stretch?  "))

    #create the threads for this program
    speech_thread = threading.Thread(target=monitor_speech)
    water_thread = threading.Thread(target=water_timer, args=(water_reminder_interval, ))
    stretch_thread = threading.Thread(target=stretch_timer, args=(stretch_reminder_interval, ))

    #start multithreading
    speech_thread.start()
    water_thread.start()
    stretch_thread.start()

main()



