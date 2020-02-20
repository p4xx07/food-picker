import logging
import os.path

#NOTSET 0
#DEBUG 10
#INFO 20
#WARNING 30
#ERROR 40
#CRITICAL 50

class Logger():
    def __init__(self, filename, level = logging.INFO):
        if(not os.path.exists(filename)):
            f = open(filename, "w")
            f.close()        
        logging.basicConfig(filename = filename, level = level, datefmt='%Y-%m-%d %H:%M:%S')

    def log(self, message, level):
        logging.log(level, message)

    def logNotSet(self, message):
        logging.log(0, message)

    def logDebug(self, message):
        logging.log(10, message)

    def logInfo(self, message):
        logging.log(20, message)

    def logWarn(self, message):
        logging.log(30, message)
        
    def logError(self, message):
        logging.log(40, message)
        
    def logCritical(self, message):
        logging.log(50, message)