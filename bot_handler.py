import configs
import telebot
import sqlite3

bot = telebot.TeleBot(configs.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def __start_handler(message: telebot.types.Message):
    telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text="Я родился",
                     reply_to_message_id=message.id,
                     reply_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=3)
                     .add(telebot.types.KeyboardButton(text='/help')))
    print("Пользователь '%s' получил сообщение '%s'" % (message.from_user.id, 'Я родился', ))


def start_polling():
    bot.polling()
