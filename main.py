from telepot.loop import MessageLoop
from bot_handler import Handler
from config import Config
from logger import Logger
from telepot import Bot
import bot_handler
import telepot
import bot_handler
import time

def start(bot: Bot, config: Config, log: Logger):
    log.logInfo("------------")
    log.logInfo("Starting Bot")
    log.logInfo("------------")

    handler = Handler(bot, config, log)
    MessageLoop(bot, handler.handle).run_as_thread()

    while 1:
        try:
            handler.sendFoodGif()
            time.sleep(30)
        except Exception as e:
            log.logError(f'Exception on main thread!\n{str(e)}')