import time
import telepot
import restaurant
from config import Config
from logger import Logger
from telepot import Bot
from telepot.loop import MessageLoop
from restaurant import RestaurantFactory

class Handler():
    def __init__(self, bot: Bot, config: Config, log: Logger):
        self.bot = bot
        self.config = config
        self.log = log
        self.restaurantFactory = RestaurantFactory(config.path)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            return
        chat_id = msg['chat']['id']
        message = msg['text'].lower()

        self.log.logInfo(f'Message\t{message}\tChatType\t{chat_type}\tChatId\t{chat_id}')        
        
        if message == '/food':
            self.sendFoodMessage(chat_id)
        else:
            self.bot.sendMessage(chat_id, 'Not a valid command. Try asking for food!')
        
    def sendFoodGif(self):
        self.log.logInfo(f'Sending food gif!\tchat_id\t{self.config.chat_id}\turl\t{self.config.gif_url}')
        self.bot.sendVideo(self.config.chat_id, self.config.gif_url)
        self.sendFoodMessage(self.config.chat_id)
        
    def sendFoodMessage(self, chat_id):
        food = self.restaurantFactory.getFood()
        self.bot.sendMessage(chat_id, food)
