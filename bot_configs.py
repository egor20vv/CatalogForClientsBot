import telebot

REMOVED_MARKUP = telebot.types.ReplyKeyboardRemove()

MAIN_PAGE_MARKUP = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False) \
    .row(telebot.types.KeyboardButton('🍭 Поиск'))\
    .row(telebot.types.KeyboardButton('🍱 Категории'),
         telebot.types.KeyboardButton('🍥 Настройки')) \
    .row(telebot.types.KeyboardButton('🍻 Помощь'),
         telebot.types.KeyboardButton('🥂 Поделиться'))

BACK_TO_MAIN_PAGE_MARKUP = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(telebot.types.KeyboardButton('↩ Вернуться'))
