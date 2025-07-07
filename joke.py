import requests


def get():
    headers = {"Accept": "text/plain"}
    f = requests.get('https://icanhazdadjoke.com', headers=headers)
    return f.text
