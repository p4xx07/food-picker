import os, inspect
import telepot
import main
from logger import Logger
from config import Config
from telepot import Bot

def getBot(token) -> Bot:
    return telepot.Bot(token)

def getConfig(working_path) -> Config:
    return Config(working_path)

def getLog(working_path) -> Logger:
    fullpath = f'{working_path}/log/logfile.log'
    return Logger(fullpath)

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
log = getLog(path)
config = getConfig(path)
bot = getBot(config.token)
main.start(bot, config, log)
