import requests
from bs4 import BeautifulSoup


# Another simple single page web scraping
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1

for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n') # Item Name has a \n character so we strip it
    itemPrice = i.find('h5').text

    print('%s) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count +=1


# find() vs. find_all()
# find(): grabs the first element with the specified tag/id and return the object as type bs4 i.e.  <p id="something1"></p>
# find_all(): grabs ALL the element with the specified tag/id and return the object as a list of type bs4 i.w. <p id="something1"></p><p id="something2"></p> etc...

print('======================================================')


# Multiple pages webscraping

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None # Will check if it is a number, else it would be 'Next' or 'Previous'

    if pageNum != None:
        x = link.get('href') # page number to append to our link
        urls.append(x)

print(urls)
print('======================================================')


# Repeat the same as single page but for all pages
count = 1
for i in urls:
    newUrl = url + i
    print('url: ' + str(newUrl))
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n') # Item Name has a \n character so we strip it
        itemPrice = i.find('h5').text

        print('%s) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count +=1
    print('\n')

    