import requests
from bs4 import BeautifulSoup

# requests library is used to create the get query
# lxml for processing the html
# Beautiful Soupp create a parsed and navigable html document

url = 'https://quotes.toscrape.com/'
response = requests.get(url) # gets the html of the website

soup = BeautifulSoup(response.text, 'lxml') # parsing response and letting BeautifuSoup know we want to use the lxml parser
print(soup)
print('==============================================================================================')


# Variable containing list of elements with the tag and class
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text + ' - ' + authors[i].text)
    
    # Tags can have more than one, so this will find all tags in the div class tag
    quote_tags = tags[i].find_all('a', class_='tag')
    
    print('tags: ')
    for tag in quote_tags:
        print(tag.text) 
