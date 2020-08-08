import requests
import json
import urllib.request

def downloadVideo(token, file_id, path):
    f = requests.get(f'https://api.telegram.org/bot{token}/getFile?file_id={file_id}')
    j = json.loads(f.text)
    file_path = j['result']['file_path']
    urllib.request.urlretrieve(f'https://api.telegram.org/file/bot{token}/{file_path}', path)