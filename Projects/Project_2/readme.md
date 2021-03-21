# Project 2

### Study tool

This is an enhancement of the hydration tool developed for Project 1. This script leverages multithreading to complete multiple tasks at the same time. There is a configurable reminder to remind the user to drink water regularly as well as a voice activated tool to search Wikipedia for information.

Python3 is required to run this app, as well as a few dependencies that will need to be installed.

To verify that python is installed, run:
```powershell
python --version
```
To install the required libraries, type:
```powershell
pip install wikipedia
pip install SpeechRecognition
pip install win10toast
```

An addtional library is required for microphone functionality, however the library (PyAudio) seems to not install correctly through pip for python versions above 3.7. To get PyAudio to work for versions above 3.7, go to https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and downloaded the .whl file for your version of python and system type (32 or 64 bit). For me, this meant downloading PyAudio-0.2.11-cp39-cp39-win_amd64.whl and dragging the file into the python project folder. I downloaded this version as my python version is 3.9 and I am on a 64 bit system.

After dragging the wheel file into the folder, open up a terminal and cd into the file's location and run:
```powershell
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```

To run the program, go to the directory that it is downloaded in and type:
```powershell
python3 Project_2.py
```
### Output
When starting up the app, the screen should prompt the user as shown below.
![startup](https://user-images.githubusercontent.com/65302404/111075637-4ec3b200-84bf-11eb-989f-643ab1ab778a.PNG)
After the prompted time has passed, a notification is shown as below.
![reminder](https://user-images.githubusercontent.com/65302404/111075635-4e2b1b80-84bf-11eb-9b47-b07d63f25185.PNG)
At any point, the user can say "Wikipedia <term>" and get wikipedia results for the text if available. Below is an example of saying "Wikipedia New York City"
![searchresult](https://user-images.githubusercontent.com/65302404/111075636-4ec3b200-84bf-11eb-88e4-450e2f853a24.PNG)

