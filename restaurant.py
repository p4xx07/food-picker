from random import randint
from datetime import datetime

def readRestaurants(path) -> {}:
    dictionary = {}
    with open(path) as f:
        i = 0
        for line in f:
            res = line.replace('\n', '')
            print(res)
            dictionary[int(i)] = res
            i += 1
    return dictionary

def canSendFoodGif():
    now = datetime.now()
    weekday = now.weekday()
    if(weekday == 5 or weekday == 6):
        return -1
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    second = int(now.strftime("%S"))

    return -1
    return 1
    
class RestaurantFactory():
    def __init__(self, path):
        full_path = f'{path}/config/restaurants.dat'
        self.dictionary = readRestaurants(full_path)

    def getFood(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]