import requests
from bs4 import BeautifulSoup

página = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

beautifulSoup = BeautifulSoup(página.content, 'html.parser')

parágrafosDentroDeDiv = beautifulSoup.select("div p")
print(parágrafosDentroDeDiv)