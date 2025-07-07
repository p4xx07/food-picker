from random import randint
import os
import helper

answer_factory = None


class AnswerFactory():
    def __init__(self):
        full_path = os.getenv("ANSWER_PATH")
        self.dictionary = helper.read_as_dictionary(full_path)

    def get(self):
        random = randint(0, len(self.dictionary) - 1)
        return self.dictionary[random]


def get():
    global answer_factory
    if not answer_factory:
        answer_factory = AnswerFactory()
    return answer_factory.get()
