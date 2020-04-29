import time
import telepot
import requests
import restaurant
import meme
import os
import re
from config import Config
from logger import Logger
from telepot import Bot
from telepot.loop import MessageLoop
from restaurant import RestaurantFactory
from exclamation import ExclamationFactory

class Handler():
    def __init__(self, bot: Bot, config: Config, log: Logger):
        self.bot = bot
        self.config = config
        self.log = log
        self.restaurantFactory = RestaurantFactory(config.path)
        self.exclamationFactory = ExclamationFactory(config.path)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            return
        chat_id = msg['chat']['id']
        message = msg['text'].lower()

        self.log.logInfo(f'Message\t{message}\tChatType\t{chat_type}\tChatId\t{chat_id}')        
        
        if '/food' in message:
            self.sendFoodMessage(chat_id)
        elif '/fact' in message:
            self.sendRandomFact(chat_id)
        elif '/meme' in message:
            self.sendRandomMeme(chat_id)
        elif '/roll':
            num = re.search(r"\d+", message)
            if num is not None:
                return
            sides = message[num.start():num.end()]
            self.sendRoll(chat_id, int(sides))
        else:
            self.sendExclamation(chat_id)
        
    def sendFoodGif(self):
        self.log.logInfo(f'Sending food gif!\tchat_id\t{self.config.chat_id}\turl\t{self.config.gif_url}')
        self.bot.sendVideo(self.config.chat_id, self.config.gif_url)
        #self.sendFoodMessage(self.config.chat_id)
        #self.sendRandomFact(self.config.chat_id)
        self.sendRandomMeme(self.config.chat_id)

    def sendFoodMessage(self, chat_id):
        food = self.restaurantFactory.getFood()
        self.bot.sendMessage(chat_id, food)

    def sendRandomFact(self, chat_id):
        f = requests.get('https://uselessfacts.jsph.pl/random.txt?language=en')
        text = f.text.split("\n")[0]
        text = text.replace("> ", "")
        self.log.logInfo(text)
        self.bot.sendMessage(chat_id, text)

    def sendExclamation(self, chat_id):
        exclamation = self.exclamationFactory.getExclamation()
        self.bot.sendMessage(chat_id, exclamation)

    def sendRandomMeme(self, chat_id):
        image = meme.generateMeme()
        image.save("img.png")
        file = open('img.png', 'rb')
        self.bot.sendPhoto(chat_id, photo=file)

    def sendRoll(self, chat_id, sides: int):
        import roll
        value = roll.roll(sides)
        self.log.logInfo(str(value))
        self.bot.sendMessage(chat_id, str(value))

        if(value == 20):
            self.bot.sendMessage(chat_id, "CRITICALLLLL!!!!")
        elif(value == 1):
            self.bot.sendMessage(chat_id, "RIP")
