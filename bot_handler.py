import configs
import telebot
import sqlite3
import bot_configs
import user
import reporter


# bot init
bot = telebot.TeleBot(configs.TOKEN, parse_mode=None)


# start
@bot.message_handler(commands=['start'])
def __start_handler(message: telebot.types.Message):
    user.set_user(message.from_user.id)
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
    print("Пользователь '{}' перешел к поиску".format(reporter.get_user_id(message)))


# go to categories
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🍱 Категории')
def __categories_handler(message: telebot.types.Message):
    # TODO release categories
    text = 'Ну это категории'
    bot.send_message(message.chat.id,
                     text=text,
                     reply_markup=bot_configs.BACK_TO_MAIN_PAGE_MARKUP)
    print("Пользователь '{}' перешел к категориям".format(reporter.get_user_id(message)))


# go to help
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🍻 Помощь')
def __help_handler(message: telebot.types.Message):
    show_help(message)


# go to help 2
@bot.message_handler(commands=['help'])
def __help_handler2(message: telebot.types.Message):
    show_help(message)


# @bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
# def settings_respond_handler(chosen_inline_result: telebot.types.ChosenInlineResult):
#     print('chosen_inline_result: \n' + str(chosen_inline_result))
#
#
# @bot.inline_handler(func=lambda query: True)
# def settings_respond_handler1(query):
#     print('Полученный результат:')
#     print('type = ' + str(type(query)))
#     print('value = ' + str(query))


# go to settings
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🍥 Настройки')
def __settings_handler(message: telebot.types.Message):
    print("Пользователь '{}' перешел к настройкам".format(reporter.get_user_id(message)))

    # TODO release settings

    markup = get_settings_markup(message.from_user.id)

    text = '🍥 Настройки'
    bot.send_message(message.chat.id, text=text, reply_markup=markup)


# respond on changing settings
@bot.callback_query_handler(func=lambda callback: 's:' in callback.data)
def __settings_callback_respond(callback: telebot.types.CallbackQuery):
    s_value = int(str(callback.data)[2])
    s_number_string = str(callback.data)[0:3]

    actual_value = user.turn_setting_sn(callback.from_user.id, s_value=s_value)

    markup = get_settings_markup(callback.from_user.id)

    try:
        bot.edit_message_reply_markup(callback.message.json['chat']['id'],
                                      callback.message.message_id,
                                      callback.inline_message_id,
                                      reply_markup=markup)

        print("Пользоватеь '{}' изменил параметр '{}' на значение '{}'"
              .format(callback.from_user.id, s_number_string, actual_value))
    except telebot.apihelper.ApiTelegramException as e:
        print("Пользователю '{}' не удалось изменить параметр {}: {}"
              .format(callback.from_user.id, s_number_string, e))


# go to share
@bot.message_handler(content_types=['text'], func=lambda message: message.text == '🥂 Поделиться')
def __share_handler(message: telebot.types.Message):
    # TODO release share
    text = 'Ну тут ты будешь дулиться ботом, вот бы кто реализвал...'
    bot.send_message(message.chat.id,
                     text=text)
    print("Пользователь '{}' возжелал поделиться ботом, какой молодец".format(reporter.get_user_id(message)))


# Respond on search
@bot.message_handler(content_types=['text'])
def __text_handler(message: telebot.types.Message):
    print("Пользователь '{}' отправил '{}'".format(reporter.get_user_id(message), message.text, ))
    bot.send_message(message.chat.id, text='Да, я умею обрабатывать текст, и что? А А А А А?',
                     reply_to_message_id=message.message_id)


def show_help(message: telebot.types.Message):
    bot.send_message(message.chat.id,
                     "Мы не нашли как помочь иначе, "
                     "кроме как дать контакты психиатра @EgorVv21")
    print("Пользователь '{}' удачно получил контакты психиатра".format(reporter.get_user_id(message)))


def show_main_page(message: telebot.types.Message):
    text = "Это главная страница"
    bot.send_message(message.chat.id, text=text,
                     reply_markup=bot_configs.MAIN_PAGE_MARKUP)
    print("Пользователь '{}' перешел на главную страницу".format(reporter.get_user_id(message)))


def get_settings_markup(user_id: int) -> telebot.types.InlineKeyboardMarkup:
    settings = user.get_settings(user_id)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton('Записей на странице: {}'
                                                  .format(10 if settings['s0'] else 5),
                                                  callback_data="s:0{}".format(int(settings['s0']))))
    markup.row(telebot.types.InlineKeyboardButton('Показывать товары той же категории: {}'
                                                  .format('Нет' if settings['s1'] else 'Да'),
                                                  callback_data="s:1{}".format(int(settings['s1']))))
    if settings['s1'] is False:
        markup.row(telebot.types.InlineKeyboardButton('🔼 Количество отображаемых полей: {}'
                                                      .format(4 if settings['s2'] else 2),
                                                      callback_data='s:2{}'.format(int(settings['s2']))))
    markup.row(telebot.types.InlineKeyboardButton('Показывать товары \'С этим покапают\': {}'
                                                  .format('Нет' if settings['s3'] else 'Да'),
                                                  callback_data="s:3{}".format(int(settings['s3']))))
    if settings['s3'] is False:
        markup.row(telebot.types.InlineKeyboardButton('🔼 Количество отображаемых полей: {}'
                                                      .format(4 if settings['s4'] else 2),
                                                      callback_data='s:4{}'.format(int(settings['s4']))))
    return markup


def start_polling():
    bot.polling()
