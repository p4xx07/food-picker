from random import randint
import os
import helper

software_factory = None


class SoftwareFactory():
    def __init__(self):
        full_path = os.getenv("SOFTWARE_PATH")
        self.dictionary = helper.read_as_dictionary(full_path)

    def get(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]


def get():
    global software_factory
    if not software_factory:
        software_factory = SoftwareFactory()
    return software_factory.get()
