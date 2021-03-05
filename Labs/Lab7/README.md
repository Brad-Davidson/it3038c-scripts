# Lab 7

### WWikipedia Library Sample

This app is meant to showcase the wikipedia library for python3.

Python3 is required to run this app, as well as an additional dependency for the wikipedia library.

To verify that python is installed, run:
```powershell
python --version
```
To install the wikipedia library, type:
```powershell
pip install wikipedia
```

To run the program, go to the directory that it is downloaded in and type:
```powershell
python3 Lab7.py
```
### Output
After starting the program, you can view the commands available by running the 'help' command.
![helpPic](https://user-images.githubusercontent.com/65302404/110148276-a28d1780-7daa-11eb-8ffb-e40c00d1057b.PNG)
running the page command as seen below will return the content of that topic's wiki page. If the term is ambiguous, it will prompt for a more specific term. Warning: this may take a few seconds.
![pagePic](https://user-images.githubusercontent.com/65302404/110148278-a28d1780-7daa-11eb-9d42-35705c163a71.PNG)
If you want a more concise overview of a specific topic, you can run the summary command. This will return a summary of the topic in a block of text, rather than the entire page.
![summaryPic](https://user-images.githubusercontent.com/65302404/110148280-a28d1780-7daa-11eb-85a3-6cdd35f813d8.PNG)
If you want to get the topic available, run the search command to get a list of related topics.
![searchPic](https://user-images.githubusercontent.com/65302404/110148279-a28d1780-7daa-11eb-8fe0-b383cb175289.PNG)

Documentation for the Wikipedia library can be found at https://wikipedia.readthedocs.io/en/latest/quickstart.html


To stop this program, either close the command terminal or press ctrl + C
