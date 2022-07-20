import requests
import json
import urllib.request
from random import randint
import os

def save_audio(url):
    random = str(randint(0, 999999))
    filename = random + '.wav'
    os.system('ffmpeg -i ' + url + ' ' + filename)
    return filename