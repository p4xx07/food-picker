from telepot.loop import MessageLoop
from bot_handler import Handler
from config import Config
from logger import Logger
from telepot import Bot
import datetime
import bot_handler
import telepot
import bot_handler
import time

def start(bot: Bot, config: Config, log: Logger):
    log.logInfo("------------Starting Bot------------")
    handler = Handler(bot, config, log)
    MessageLoop(bot, handler.handle).run_as_thread()

    while True:
        try:
            if(canSendFoodGif()):
                handler.sendFoodGif()
            time.sleep(30)
        except Exception as e:
            log.logError(f'Exception on main thread!\n{str(e)}')
            time.sleep(15)

def canSendFoodGif() -> bool:
    now = datetime.datetime.now()
    weekday = now.weekday()
    if(weekday >= 5):
        return False
    mid_day = datetime.datetime(now.year, now.month, now.day, 12, 30)    
    diff_seconds = (now - mid_day).total_seconds()    
    return diff_seconds > 0 and diff_seconds < 45