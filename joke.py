import requests
import json

def get():
    f = requests.get('https://official-joke-api.appspot.com/random_joke')
    jsonData = json.loads(f.text)
    return jsonData['setup'] + '\n' + jsonData['punchline']
