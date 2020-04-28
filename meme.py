import requests
from random import randint

import json
from PIL import Image, ImageDraw, ImageFont


import io
import re


def getSubmission():
    f = requests.get('http://alpha-meme-maker.herokuapp.com/submissions/')
    jsonSubmissions = json.loads(f.text)
    length = len(jsonSubmissions['data'])
    num = randint(0, length - 1)
    return jsonSubmissions['data'][num]

def getMemeImage(memeID):
    f = requests.get('http://alpha-meme-maker.herokuapp.com/memes/' + str(memeID))
    jsonMeme = json.loads(f.text)
    url = jsonMeme['data']['image']
    r = requests.get(url)
    return r.content
 
def drawText(draw, x, y, text, font, color, shadow):
    # thin border
    draw.text((x-1, y), text, fill=shadow)
    draw.text((x+1, y), text, fill=shadow)
    draw.text((x, y-1), text, fill=shadow)
    draw.text((x, y+1), text, fill=shadow)

    # thicker border
    draw.text((x-1, y-1), text, fill=shadow)
    draw.text((x+1, y-1), text, fill=shadow)
    draw.text((x-1, y+1), text, fill=shadow)
    draw.text((x+1, y+1), text, fill=shadow)

    #normal    
    draw.text((x, y), text, fill=color)


def wrap_by_word(s, n):
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

def getImageWithText(content, top, bottom):
    with io.BytesIO(content) as f:
        with Image.open(f) as img:
            draw = ImageDraw.Draw(img)
            #font = ImageFont.truetype("arial.ttf", 25)

            width, height = img.size
            shadow = "black"
            color = "white"
            top = wrap_by_word(top, 6)
            bottom =  wrap_by_word(bottom, 6)
            drawText(draw, 10, 15, top, "", color, shadow)
            drawText(draw, 10, height - 100, bottom, "", color, shadow)
            return img

def generateMeme():
    submission = getSubmission()
    content = getMemeImage(submission['memeID'])
    finalImage = getImageWithText(content, submission['topText'], submission['bottomText'])
    return finalImage
