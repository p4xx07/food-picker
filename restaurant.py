from random import randint
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
    
class RestaurantFactory():
    def __init__(self, path):
        full_path = f'{path}/config/restaurants.dat'
        self.dictionary = readRestaurants(full_path)

    def getFood(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]