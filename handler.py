import os, inspect
import datetime
import time

import dante as Dante
import answer as Answer
import software as Software
import markov as Markov
import roll as Roll
import joke as Joke
import fact as Fact
import exclamation as Exclamation

def dante(update, context): 
    phrase = Dante.get()
    context.bot.send_message(chat_id=update.effective_chat.id, text=phrase, parse_mode='Markdown')

def answer(update, context): 
    text = Answer.get()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def software(update, context): 
    text = Software.get()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def potter(update, context): 
    text = Markov.get_potter(50)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def roll(update, context): 
    sides = 20
    value = Roll.roll(sides)
    if(value == sides):
        context.bot.send_message(chat_id=update.effective_chat.id, text="CRITICALLL!!")
    elif(value == 1):
        context.bot.send_message(chat_id=update.effective_chat.id, text="RIP")
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(value))

def joke(update, context): 
    text = Joke.get()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def fact(update, context): 
    text = Fact.get()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def unknown(update, context):
    text = Exclamation.get()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def test_food_gif(bot, gif):
    send_food_gif(bot, gif, 146470365)
    
def send_food_gif(bot, gif, chat_id):
    bot.send_animation(chat_id=chat_id, animation=gif)
    phrase = Dante.get()
    bot.send_message(chat_id=chat_id, text=phrase, parse_mode='Markdown')

def restarted(bot):
    bot.send_message(chat_id=146470365, text="Restarted!")

def reminder(bot, gif, chat_id):
    hour = -1 
    while True:
        if can_send_food_gif():
            send_food_gif(bot, gif, chat_id)
        now_hour = int(datetime.datetime.now().hour)
        if  hour < now_hour and now_hour >= 9 and now_hour <= 21:
            hour = now_hour
            #TODO IMPLEMENT handler.sendWater()
        time.sleep(32)

def can_send_food_gif() -> bool:
    now = datetime.datetime.now()
    mid_day = datetime.datetime(now.year, now.month, now.day, 12, 30)    
    diff_seconds = (now - mid_day).total_seconds()    
    return diff_seconds > 0 and diff_seconds <= 32
