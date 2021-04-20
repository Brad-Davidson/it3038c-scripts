import sys
import textwrap
import re
import numpy as np
import cv2
from PIL import Image
import types
from stegano import lsb

# Project 3
# Bradley Davidson

#the size of each letter picture in the images folder
CONST_IMAGE_SIZE = (72, 74)

#function for hiding the english translation into the picture
def encode_picture(text, image_location):
    #using the stegano library's "Least Significant Bit" algorithm
    secret = lsb.hide(image_location, text)
    secret.save(image_location)

#function to decode the image to get the english translation
def showText(image_location):
    message = lsb.reveal(image_location)
    return str(message)

#rules for what to do on the letter "C", as there is no letter C in this alphabet
def determine_C(next_letter):
    if next_letter in ["e", "i", "y"]:
        return "Images/S.png"
    else:
        return "Images/K.png"

#create the full picture of all of the rune letters
def encode_to_dragon(text, image_location):
    #Make all of the text uppercase as there is no distinction between upper and lower case in this language
    text_upper = text.upper()
    #remove anything that isn't a letter from the text
    text_upper = re.sub(r'[^\w\s]','', text_upper)

    #create an array of text lines that are all 20 characters or less
    wrapper = textwrap.TextWrapper(width=20)
    word_list = wrapper.wrap(text=text_upper)

    #get the total size that the image will be
    total_width = CONST_IMAGE_SIZE[0]
    total_height = CONST_IMAGE_SIZE[1] * len(word_list)

    #create a blank image witht he appropriate size
    rune_image = Image.new('RGB', (total_width, total_height))

    x_offset = 0
    y_offset = 0
    #fill that image with the rune images
    for line in word_list:
        for index, letter in enumerate(line): #get each character within a sentence
            if letter != " ":
                if letter == "C":
                    if index + 1 < len(line):
                        image_string = determine_C(line[index + 1]) #send the next character, as that determines what the C sound is
                    else:
                        image_string = determine_C(" ")
                else:
                    image_string = "Images/" +letter + ".png" #file location for all the leters
                new_image = Image.open(image_string)
                #paste the appropriate image at its given space on the canvas
                rune_image.paste(new_image, (x_offset, y_offset))
            #move the pointer for the x position for the image
            x_offset += CONST_IMAGE_SIZE[0]
        #reset the x pointer as its a new line
        x_offset = 0
        #increment the y pointer so that it goes to the next line
        y_offset += CONST_IMAGE_SIZE[1]
    try:    
        #create a cv2 image and send it to be encoded
        cv2_rune_image = cv2.cvtColor(np.array(rune_image), cv2.COLOR_RGB2BGR)
        cv2.imwrite(image_location, cv2_rune_image)
        encode_picture(text_upper, image_location)
    except:
        print("Could not write a file to that location.")

while True:
    prompt = input("""
    What would you like to do?
    1. Translate to Dragon Runes
    2. Translate Dragon Runes to English
    Answer: """)

    if prompt == "1":
        message_to_encode = input("Text to translate: ")
        #if there is any numbers, reprompt as there is no way to translate numbers
        if(any(char.isdigit() for char in message_to_encode)):
            print("Please don't use numbers")
        else:
            image_location = input("Where should the image go? (Note: save file as .png): ")
            encode_to_dragon(message_to_encode, image_location)
    elif prompt == "2":
        image_location = input("Location of image to translate (only works with .png): ")
        try:
            image = cv2.imread(image_location)
            print("Translated Text: " + showText(image_location))
        except:
            print("file not found")
    else:
        print("Invalid answer")

#############################################
# Resources Used ############################
#############################################
# Getting if a string has a number: https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
# Stegano Library: https://pypi.org/project/stegano/
# How to mess with images and their pixel values: https://pypi.org/project/opencv-python/
#
#