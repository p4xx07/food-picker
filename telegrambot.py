import sys
import time
import telepot
from random import seed
from random import randint
from datetime import datetime

homerFoodUrl = "https://i.pinimg.com/originals/01/e3/33/01e3334038b010ef6c845c3f0fe7ab7d.gif"
msChatId = "-283832797"
d = {}


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("error")
    return conn

def select_all_restaurants(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurants")
    rows = cur.fetchall()
    return rows

def readRestaurants():
    print('Reading restaurants')
    with open("/home/pi/Documents/TelegramBot/restaurants.dat") as f:
        i = 0
        for line in f:
            res = line.replace('\n', '')
            print(res)
            d[int(i)] = res
            i += 1

def getFood():
    print('Gathering food')
    random = getRandom(0, len(d))
    print('Found -> ' + d[random])
    return d[random]

def getRandom(min, max):
    for _ in range(max - 1):
        value = randint(min, max - 1)
        print(value)
        return value

def log(text):
    f = open("/home/pi/Documents/TelegramBot/log.txt", "a")
    f.write(text + "\n")
    f.close()

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()
    log(str(chat_id)+ " - " + msg['text'])
    if command == '/food' or 'food' in command:
        food = getFood()
        bot.sendMessage(chat_id, food)
    else:
        bot.sendMessage(chat_id, 'Not a valid command. Try asking for food!')


bot = telepot.Bot('1071858466:AAHmgyryCUd0qv2FPkQ1WJHwv8tdKwk_S4c')
restaurantList = readRestaurants()

#database = "/home/pi/Documents/TelegramBot/telegram.db"
#conn = create_connection(database)
#with conn:
#    print("1. Query task by priority:")
#    rows = select_all_restaurants(conn)
#    for r in rows:
#        print(r)

bot.message_loop(handle)
print('Starting bot')
while 1:
    try:
       sendFoodGif()
       time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occured!')

def sendFoodGif():
    weekday = datetime.today().weekday()
    if(weekday == 5 or weekday == 6):
        return
    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    if(hour == "12" and minute == "30"):
        bot.sendVideo(msChatId, homerFoodUrl)
