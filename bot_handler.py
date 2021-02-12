import configs
import telebot
import sqlite3
import bot_configs


# bot init
bot = telebot.TeleBot(configs.TOKEN, parse_mode=None)


# start
@bot.message_handler(commands=['start'])
def __start_handler(message: telebot.types.Message):
    show_help(message)
    show_main_page(message)


# go to main page
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '↩ Вернуться')
def __back_to_main_page(message: telebot.types.Message):
    show_main_page(message)


# go to search
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🍭 Поиск')
def __search_handler(message: telebot.types.Message):
    # TODO release search
    text = 'Ну это поиск'
    bot.send_message(message.chat.id,
                     text=text,
                     reply_markup=bot_configs.BACK_TO_MAIN_PAGE_MARKUP)
    print("Пользователь '{}' перешел к поиску".format(get_user_id(message)))


# go to categories
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🍱 Категории')
def __categories_handler(message: telebot.types.Message):
    # TODO release categories
    text = 'Ну это категории'
    bot.send_message(message.chat.id,
                     text=text,
                     reply_markup=bot_configs.BACK_TO_MAIN_PAGE_MARKUP)
    print("Пользователь '{}' перешел к категориям".format(get_user_id(message)))


# go to help
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🍻 Помощь')
def __help_handler(message: telebot.types.Message):
    show_help(message)


# go to help 2
@bot.message_handler(commands=['help'])
def __help_handler2(message: telebot.types.Message):
    show_help(message)


# go to settings
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🍥 Настройки')
def __settings_handler(message: telebot.types.Message):
    # TODO release settings
    text = 'Ну это настройки'
    bot.send_message(message.chat.id,
                     text=text,
                     reply_markup=bot_configs.BACK_TO_MAIN_PAGE_MARKUP)
    print("Пользователь '{}' перешел к настройкам".format(get_user_id(message)))


# Respond on search
@bot.message_handler(content_types=['text'])
def __text_handler(message: telebot.types.Message):
    print("Пользователь '{}' отправил '{}'".format(get_user_id(message), message.text, ))
    bot.send_message(message.chat.id, text='Да, я умею обрабатывать текст, и что? А А А А А?',
                     reply_to_message_id=message.message_id)


def get_user_id(message: telebot.types.Message) -> str:
    return "[{}, {}]".format(message.from_user.id, message.from_user.username, )


def show_help(message: telebot.types.Message):
    bot.send_message(message.chat.id,
                     "Мы не нашли как помочь иначе, "
                     "кроме как дать контакты психиатра @EgorVv21")
    print("Пользователь '{}' удачно получил контакты психиатра".format(get_user_id(message)))


def show_main_page(message: telebot.types.Message):
    text = "Это главная страница"
    bot.send_message(message.chat.id, text=text,
                     reply_markup=bot_configs.MAIN_PAGE_MARKUP)
    print("Пользователь '{}' перешел на главную страницу".format(get_user_id(message)))


def start_polling():
    bot.polling()
