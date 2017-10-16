import requests
from bs4 import BeautifulSoup

página = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

beautifulSoup = BeautifulSoup(página.content, 'html.parser')

paragrafosComAClasseOuterText = beautifulSoup.find_all('p', class_='outer-text')
elementosComAClasseOuterText = beautifulSoup.find_all(class_="outer-text")
elementosComIdFirst = beautifulSoup.find_all(id="first")

print(paragrafosComAClasseOuterText)
print(elementosComAClasseOuterText)
print(elementosComIdFirst)