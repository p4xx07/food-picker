import requests
import json
from bs4 import BeautifulSoup as Soup

def getDante():
    html = requests.get("https://accademiadellacrusca.it/it/dante")
    soup = Soup(html.content, "html.parser")
    word = soup.select('div.col-12 h3 i')[0].text
    subword = soup.select('div.col-12 p')[0].text
    verse = soup.select('div.col-12 blockquote')[0].get_text(separator='\n')
    description = soup.select('div.col-12 p')[2].text
    return (word.capitalize(), subword, verse, description)

