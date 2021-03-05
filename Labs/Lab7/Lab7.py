import wikipedia
import warnings

# Lab 7
# Bradley Davidson
# Wiki library showcase
# Description: Showcase the "search", "summary", and "page" functionality of the wiki library

warnings.catch_warnings()
warnings.simplefilter("ignore") #This is to ignore a warning thrown by the wikipedia library, as other errors are being manually caught

#Display the commands associated with this program
def display_help():
    print('''Commands for Wikipedia api
    help: display commands for this project.
    summary <term>: display a summary for the term provided.
    search <term>: search for pages related to the term.
    page <term>: gets page info from a page based on the term.
    ''')

# Display a summary of a specific wiki page
def display_summary(term):
    try:
        print(wikipedia.summary(term))
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous term, select one of the terms below:")
        print(e.options)

#display search results based off of a provided key word
def display_search(term):
    try:
        print("Search Terms: " + str(wikipedia.search(term)))
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous term, select one of the terms below:")
        print(e.options)

#display the contents of a specific wiki page. If a page isn't found, show possible suggested pages.
def display_page(term):
    try:
        page = wikipedia.page(term)
        print(f''' Wiki Page: {page.title}
        URL: {page.url}
        Content: 
        {page.content}
        ''')
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous term, select one of the terms below:")
        print(e.options)

while True:
    user_command = input("Enter a command (type 'help' to see commands): ")

    if(user_command == "help"):
        display_help()
    #splitting the string so that the first word acts as a command while all of the following words act as arguements
    elif(user_command.split()[0] == "summary"):
        if(len(user_command.split()) > 1):
            display_summary(user_command.split(' ', 1)[1])
        else:
            print("Invalid Parameter")
    elif(user_command.split()[0] == "search"):
        if(len(user_command.split()) > 1):
            display_search(user_command.split(' ', 1)[1])
        else:
            print("Invalid Parameter")
    elif(user_command.split()[0] == "page"):
        if(len(user_command.split()) > 1):
            display_page(user_command.split(' ', 1)[1])
        else:
            print("Invalid Parameter")
