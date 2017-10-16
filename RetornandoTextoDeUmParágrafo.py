import requests
from bs4 import BeautifulSoup

página = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

beautifulSoup = BeautifulSoup(página.content, 'html.parser')
html = list(beautifulSoup.children)[2]
body = list(html.children)[3]
p = list(body.children)[1]
textoDoParágrafo = p.get_text()

print(textoDoParágrafo)