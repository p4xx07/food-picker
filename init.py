import config
import handler
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

(token, gif, chat_id) = config.get()
updater = Updater(token=token)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

dante_handler = CommandHandler('dante', handler.dante)
answer_handler = CommandHandler('answer', handler.answer)
software_handler = CommandHandler('software', handler.software)
potter_handler = CommandHandler('potter', handler.potter)
roll_handler = CommandHandler('roll', handler.roll)
joke_handler = CommandHandler('joke', handler.joke)
fact_handler = CommandHandler('fact', handler.fact)
unknown_handler = MessageHandler(Filters.command, handler.unknown)

dispatcher = updater.dispatcher
dispatcher.add_handler(dante_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(software_handler)
dispatcher.add_handler(potter_handler)
dispatcher.add_handler(roll_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(fact_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

handler.restarted(updater.bot)
handler.reminder(updater.bot, gif, chat_id)

updater.idle()

