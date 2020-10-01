import os, inspect
import telepot
from bot_handler import Handler
from telepot import Bot
from telepot.loop import MessageLoop
import bot_handler
import datetime
import time
from config import getConfig

def start(bot: Bot):
    handler = Handler(bot)
    MessageLoop(bot, handler.handle).run_as_thread()
    seconds = 0
    while True:
        if canSendFoodGif():
            handler.sendFoodGif()
        time.sleep(30)
        seconds = seconds + 30
        if seconds >= 30:
            handler.sendWater()
            seconds = 0

def canSendFoodGif() -> bool:
    now = datetime.datetime.now()
    mid_day = datetime.datetime(now.year, now.month, now.day, 12, 30)    
    diff_seconds = (now - mid_day).total_seconds()    
    return diff_seconds > 0 and diff_seconds <= 32

config = getConfig()
bot = telepot.Bot(config[0])
start(bot)

