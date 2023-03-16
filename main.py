'''python
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
'''
'python\nimport telegram\nfrom telegram.ext import Updater, CommandHandler, MessageHandler, Filters\n'
'''python
bot = telegram.Bot('token=6200983090:AAGKJ8l23W0FqYhyQLjDOMOLpbTsHBU7sUs')
'''
"python\nbot = telegram.Bot('token=6200983090:AAGKJ8l23W0FqYhyQLjDOMOLpbTsHBU7sUs')\n"
'''python
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот магазина домашних кондитерских изделий Зефирка. Чем я могу Вам помочь?")

def menu(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Это наше меню:\n\nЗефир\nПирожные\nПастила")

def cake(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Готовим зефир на заказ. Чем я могу Вам помочь?")

def pastry(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="У нас есть множество различных видов пирожных. Чем я могу Вам помочь?")

def candy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="У нас есть широкий выбор пастилы. Чем я могу Вам помочь?")
'''
'python\ndef start(update, context):\n    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот магазина домашних кондитерских изделий Зефирка. Чем я могу Вам помочь?")\n\ndef menu(update, context):\n    context.bot.send_message(chat_id=update.effective_chat.id, text="Это наше меню:\n\nЗефир\nПирожные\nПастила")\n\ndef cake(update, context):\n    context.bot.send_message(chat_id=update.effective_chat.id, text="Готовим зефир на заказ. Чем я могу Вам помочь?")\n\ndef pastry(update, context):\n    context.bot.send_message(chat_id=update.effective_chat.id, text="У нас есть множество различных видов пирожных. Чем я могу Вам помочь?")\n\ndef candy(update, context):\n    context.bot.send_message(chat_id=update.effective_chat.id, text="У нас есть широкий выбор пастилы. Чем я могу Вам помочь?")\n'
'''python
updater = Updater(token='6200983090:AAGKJ8l23W0FqYhyQLjDOMOLpbTsHBU7sUs', use_context=True)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('menu', menu))
dispatcher.add_handler(CommandHandler('cake', cake))
dispatcher.add_handler(CommandHandler('pastry', pastry))
dispatcher.add_handler(CommandHandler('candy', candy))
'''
'''python
updater.start_polling()
'''


