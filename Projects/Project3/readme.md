# Project 3

### Dovah Translator 

This is a translator between english and the dragon language from the video game Skyrim. This was just an idea that I had back in high school when I was playin the game for the first time, but I never had any clue on where to start until recently. This will translate english text into an image that contains the equivalent runic letters. Additionally, those specific images can be processed by this script to get the English translation again. 

Python3 is required to run this app, as well as a few dependencies that will need to be installed.

To verify that python is installed, run:
```powershell
python --version
```
To install the required libraries, type:
```powershell
pip install opencv-python
pip install pillow
pip3 install Stegano
```
#### Note: this program works best in python version 3.8.5 due to some dependency issues for the stegano library in later versions
If you need to switch versions and are in a Anaconda environment, then run
```powershell
conda install python=3.8.5
```


To run the program, go to the directory that it is downloaded in and type:
```powershell
python3 Project3.py
```
### Output
When starting up the app, the screen should prompt the user as shown below.
![StartingPage](https://user-images.githubusercontent.com/65302404/115462357-8e856400-a1f8-11eb-84ec-06ac796c44e5.PNG)
A sample of what the input might look like for creating a rune picture (NOTE: FILE PATHS SHOULD END IN .PNG)
![SampleInput](https://user-images.githubusercontent.com/65302404/115462350-8b8a7380-a1f8-11eb-8f84-a14740727331.PNG)
The program will go and make an image that looks like the following:
![exampleimage](https://user-images.githubusercontent.com/65302404/115462422-a1983400-a1f8-11eb-90bf-f604d4739f89.png)
To translate that image back to english, give the program the file location for the image that you want to translate (NOTE: if no folder directory is given it will default to the folder that the python script is running in).
![ExampleTranslation](https://user-images.githubusercontent.com/65302404/115462387-980ecc00-a1f8-11eb-9071-0559d9a8111b.PNG)
If in either processes a file cannot be found or created at a location, a message similar to the following will appear.
![BadFileLocation](https://user-images.githubusercontent.com/65302404/115462377-93e2ae80-a1f8-11eb-9db2-bf6e10daf342.PNG)
