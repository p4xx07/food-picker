from random import randint
import os
import helper
    
exclamation_factory = None

class ExclamationFactory():
    def __init__(self):
        full_path = '/etc/food-picker/exclamations.dat'

        if os.name == 'nt':
            full_path = 'C:/Users/pc/Documents/etc/food-picker/exclamations.dat'

        self.dictionary = helper.read_as_dictionary(full_path)

    def get(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]

def get():
    global exclamation_factory
    if not exclamation_factory:
        exclamation_factory = ExclamationFactory()
    return exclamation_factory.get()

    

    
