from random import randint
import os
def readExclamations(path) -> {}:
    dictionary = {}
    with open(path, encoding="utf8") as f:
        i = 0
        for line in f:
            res = line.replace('\n', '')
            dictionary[int(i)] = res
            i += 1
    return dictionary
    
class ExclamationFactory():
    def __init__(self):
        full_path = '/etc/food-picker/exclamations.dat'

        if os.name == 'nt':
            full_path = 'C:/Users/pc/Documents/etc/food-picker/exclamations.dat'

        self.dictionary = readExclamations(full_path)

    def getExclamation(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]