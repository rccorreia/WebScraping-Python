import requests
from bs4 import BeautifulSoup

página = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

beautifulSoup = BeautifulSoup(página.content, 'html.parser')

listaDeParágrafos = beautifulSoup.find_all('p')
textoDoPrimeiroParágrafo = beautifulSoup.find_all('p')[0].get_text()
primeiraInstânciadDeUmParágrafo = beautifulSoup.find('p')

print(listaDeParágrafos)
print(textoDoPrimeiroParágrafo)
print(primeiraInstânciadDeUmParágrafo)