import handler
import os
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

token = os.getenv("TOKEN")
updater = Updater(token=token)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

js_handler = CommandHandler('js', handler.js)
csharp_handler = CommandHandler('csharp', handler.csharp)
c_handler = CommandHandler('c', handler.c)
python3_handler = CommandHandler('python3', handler.python3)
dante_handler = CommandHandler('dante', handler.dante)
answer_handler = CommandHandler('answer', handler.answer)
software_handler = CommandHandler('software', handler.software)
potter_handler = CommandHandler('potter', handler.potter)
roll_handler = CommandHandler('roll', handler.roll)
joke_handler = CommandHandler('joke', handler.joke)
fact_handler = CommandHandler('fact', handler.fact)
forward_to_group = CommandHandler('forward_to_group', handler.forward_to_group)
unknown_handler = MessageHandler(Filters.command, handler.unknown)
reply_handler = MessageHandler(
    Filters.text & (~Filters.command), handler.reply)
speech_handler = MessageHandler(
    Filters.voice & (~Filters.command), handler.speech)

dispatcher = updater.dispatcher
dispatcher.add_handler(js_handler)
dispatcher.add_handler(csharp_handler)
dispatcher.add_handler(c_handler)
dispatcher.add_handler(python3_handler)
dispatcher.add_handler(dante_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(software_handler)
dispatcher.add_handler(potter_handler)
dispatcher.add_handler(roll_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(fact_handler)
dispatcher.add_handler(forward_to_group)
dispatcher.add_handler(reply_handler)
dispatcher.add_handler(speech_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

handler.restarted(updater.bot)
# handler.reminder(updater.bot, gif, chat_id)

updater.idle()
