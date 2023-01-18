import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

UID_PATH = '../frizacidbox/data/uid_list.txt'
IMG_PATH = '../frizacidbox/image/dream/'

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(ascitime)s - %(name))s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm your acidBot tell me your secret")

def sendImage(update, context):
    #read uids from disk
    with open(UID_PATH) as file:
        uid_list = file.readlines()
    #remove whitespaces \n
    uid_list = [x.strip() for x in uid_list]
    print(update.message.text)
    recieved_text = update.message.text
    #check if sent message is uid of photo
    if recieved_text in uid_list:
        image = open(IMG_PATH + recieved_text + ".jpg", 'rb')
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Password incorrect...")

start_handler = CommandHandler('start', start)
sendImage_handler = MessageHandler(Filters.text, sendImage)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sendImage_handler)

updater.start_polling()
