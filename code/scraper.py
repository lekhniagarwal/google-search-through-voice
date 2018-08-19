#it takes text and make it google url and then apply webscraping 

import requests
from bs4 import BeautifulSoup

search_item = 'what is python'  ## search query
url = "https://www.google.co.in/search?q=" + search_item

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

for item in soup.select(".r a"): # soup.select(".r a")  will  give heading of all options comes while searching
    print (item.text)
    break
