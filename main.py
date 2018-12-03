import telebot
from YarovoiMuteBot import config
import telebot.types as types
from threading import Thread
import time
import random

bot = telebot.TeleBot(config.TOKEN)
count = 0


def sl():
    global count
    while True:
        time.sleep(60 * 60)
        count = 0


def run_delay():
    t = Thread(target=sl)
    t.start()


@bot.message_handler(content_types=["photo", 'gif'])
def ban_yarovoi(mess: types.Message):
    global count
    if str(mess.from_user.id) == config.YAROVOI_ID:
        count += 1
        if count == 3:
            bot.restrict_chat_member(mess.chat.id, mess.from_user.id, until_date=5000 * 60,
                                     can_send_media_messages=False)
            count = 0
            bot.reply_to(message=mess, text=random.choice(config.ANSWERS))


run_delay()
print("polling started")
bot.polling(none_stop=True)
