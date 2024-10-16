import requests
from bs4 import BeautifulSoup
from LxmlSoup import LxmlSoup


with open("magic.html", encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, "html.parser")


links = soup.find_all('a', class_='cards_list__item-wrapper')

links_magic:list = []
for link in links:
    url = link.get("href")
    links_magic.append(url)

for link in links_magic:
    req = requests.get('link').text
    
    


    


