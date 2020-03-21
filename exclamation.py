from random import randint
def readExclamations(path) -> {}:
    dictionary = {}
    with open(path, encoding="utf8") as f:
        i = 0
        for line in f:
            res = line.replace('\n', '')
            print(res)
            dictionary[int(i)] = res
            i += 1
    return dictionary
    
class ExclamationFactory():
    def __init__(self, path):
        full_path = f'{path}/config/exclamations.dat'
        self.dictionary = readExclamations(full_path)

    def getExclamation(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]