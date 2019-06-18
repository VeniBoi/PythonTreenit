import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.juvenes.fi/skene').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div'):
    #foodname = article.div.text
    print(article)



#print(soup.prettify())
