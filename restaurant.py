from random import randint
import os
def readRestaurants(path) -> {}:
    dictionary = {}
    with open(path, encoding="utf8") as f:
        i = 0
        for line in f:
            res = line.replace('\n', '')
            dictionary[int(i)] = res
            i += 1
    return dictionary
    
class RestaurantFactory():
    def __init__(self):
        full_path = '/etc/food-picker/restaurants.dat'

        if os.name == 'nt':
            full_path = 'C:/Users/pc/Documents/etc/food-picker/restaurants.dat'

        self.dictionary = readRestaurants(full_path)

    def getFood(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]