import requests
import json
from bs4 import BeautifulSoup as Soup

def getDante():
    html = requests.get("https://accademiadellacrusca.it/it/dante")
    soup = Soup(html.content, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n" + br.text)
    word = soup.select('div.col-12 h3 i')[0].text
    subword = soup.select('div.col-12 p')[0].text
    verse = soup.select('div.col-12 blockquote p')[0].text
    description = soup.select('div.col-12 p')[2].text
    return (word, subword, verse, description)

