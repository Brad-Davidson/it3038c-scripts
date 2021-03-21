#Bradley Davidson
# Lab 8
# Quote Generator: Pulls quotes from brainyquote's inspirational section randomly
import requests, re 
import random
from bs4 import BeautifulSoup 
r = requests.get("https://www.brainyquote.com/topics/inspirational-quotes").content 
soup = BeautifulSoup(r, "lxml") 
quotes = soup.findAll("div", {"class":re.compile('clearfix')})

while True:
    selected_quote = random.choice(quotes)
    quote_text = selected_quote.findAll('a', {'class':re.compile('b-qt')})[0].string
    quote_author = selected_quote.findAll('a', {'class':re.compile('bq-aut')})[0].string
    print(f"{quote_text} - {quote_author}")
    response = input("Would you like another quote? (y/n): ")
    if(response != "y"):
        break
