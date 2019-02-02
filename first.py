import requests
from bs4 import BeautifulSoup


def links(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a', href=True):
        snn = link['href']
        print(snn)
links('https://docs.python.org/3/library/functions.html')