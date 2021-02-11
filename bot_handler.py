import configs
import telebot
import sqlite3

bot = telebot.TeleBot(configs.TOKEN, parse_mode=None)


REMOVED_MARKUP = telebot.types.ReplyKeyboardRemove()

MAIN_PAGE_MARKUP = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(telebot.types.KeyboardButton('🍭 Поиск'),
         telebot.types.KeyboardButton('🍱 Категории'))\
    .row(telebot.types.KeyboardButton('🍻 Помощь'),
         telebot.types.KeyboardButton('🍥 Настройки'))


@bot.message_handler(commands=['start'])
def __start_handler(message: telebot.types.Message):
    telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text="Я родился",
                     reply_to_message_id=message.id,
                     reply_markup=MAIN_PAGE_MARKUP)
    print("Пользователь '%s' получил сообщение '%s'" % (message.from_user.id, 'Я родился', ))


@bot.message_handler(content_types=['text'])
def __text_handler(message: telebot.types.Message):
    print("Пользователь '%s' отправил '%s'", (message.from_user.id, message.text, ))


def start_polling():
    bot.polling()
