import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[2]
body = list(html.children)[3]
p = list(body.children)[1]
textoDoParagrafo = p.get_text()

print(textoDoParagrafo)