import configs
import telebot
import sqlite3

bot = telebot.TeleBot(configs.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def __start_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Я родился", reply_to_message_id=message.id)


def start_polling():
    bot.polling()
