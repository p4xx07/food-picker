from random import randint

def roll20():
    return roll(20)

def roll(sides: int):
    return randint(1, sides)