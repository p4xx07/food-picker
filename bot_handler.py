import time
import telepot
import requests
import download
import restaurant
import meme
import os
import trim
import re
from logger import Logger
from telepot import Bot
from telepot.loop import MessageLoop
from restaurant import RestaurantFactory
from exclamation import ExclamationFactory
from config import getConfig

class Handler():
    def __init__(self, bot: Bot):
        self.bot = bot
        self.restaurantFactory = RestaurantFactory()
        self.exclamationFactory = ExclamationFactory()
        self.config = getConfig()
        self.token = self.config[0]
        self.chat_id = self.config[1]
        self.gif_url = self.config[2]

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        
        if content_type == 'text':          
            self.textMessage(msg)
        elif content_type == 'video':
            self.videoMessage(msg)
        else:
            chat_id = msg['chat']['id']
            self.sendExclamation(chat_id)

    def textMessage(self, msg):
        chat_id = msg['chat']['id']
        message = msg['text'].lower()

        if '/food' in message:
            self.sendFoodMessage(chat_id)
        elif '/fact' in message:
            self.sendRandomFact(chat_id)
        elif '/meme' in message:
            self.sendRandomMeme(chat_id)
        elif '/roll' in message:
            num = re.search(r"\d+", message)
            if num is None:
                self.sendRoll(chat_id, 20)
                return
            sides = message[num.start():num.end()]
            self.sendRoll(chat_id, int(sides))
        elif '/joke' in message:
            self.sendRandomJoke(chat_id)
        elif '/tree' in message:
            self.sendRandomTree(chat_id)
        else:
            self.sendExclamation(chat_id)
    
    def videoMessage(self, msg):

        chat_id = msg['chat']['id']
        video = msg['video']
       # caption = msg['caption']

        download.downloadVideo(self.token, video["file_id"], r"video.mp4")
        trim.trimVideoToGif("video.mp4", 1,2)
        self.sendTrimToGif(chat_id)

    def sendFoodGif(self):
        self.bot.sendVideo(self.chat_id, self.gif_url)
        #self.sendFoodMessage(self.config.chat_id)
        #self.sendRandomFact(self.config.chat_id)
        #self.sendRandomMeme(self.config.chat_id)
        self.sendRandomJoke(self.chat_id)

    def sendFoodMessage(self, chat_id):
        food = self.restaurantFactory.getFood()
        self.bot.sendMessage(chat_id, food)

    def sendRandomFact(self, chat_id):
        f = requests.get('https://uselessfacts.jsph.pl/random.txt?language=en')
        text = f.text.split("\n")[0]
        text = text.replace("> ", "")
        self.bot.sendMessage(chat_id, text)

    def sendExclamation(self, chat_id):
        exclamation = self.exclamationFactory.getExclamation()
        self.bot.sendMessage(chat_id, exclamation)

    def sendRandomMeme(self, chat_id):
        image = meme.generateMeme()
        image.save("img.png")
        file = open('img.png', 'rb')
        self.bot.sendPhoto(chat_id, photo=file)

    def sendRandomTree(self, chat_id):
        import draw
        draw.generateTree()
        file = open('img/tree.gif', 'rb')
        self.bot.sendVideo(chat_id, video=file)

    def sendRoll(self, chat_id, sides: int):
        import roll
        value = roll.roll(sides)
        self.bot.sendMessage(chat_id, str(value))

        if(value == sides):
            self.bot.sendMessage(chat_id, "CRITICALLLLL!!!!")
        elif(value == 1):
            self.bot.sendMessage(chat_id, "RIP")

    def sendRandomJoke(self, chat_id):
        import joke
        value = joke.getRandomJoke()
        self.bot.sendMessage(chat_id, str(value))

    def sendTrimToGif(self, chat_id):
        file = open('output.gif', 'rb')
        self.bot.sendVideo(chat_id, video=file)