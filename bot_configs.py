import telebot

REMOVED_MARKUP = telebot.types.ReplyKeyboardRemove()

MAIN_PAGE_MARKUP = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(telebot.types.KeyboardButton('🍭 Поиск'),
         telebot.types.KeyboardButton('🍱 Категории')) \
    .row(telebot.types.KeyboardButton('🍻 Помощь'),
         telebot.types.KeyboardButton('🍥 Настройки'))

BACK_TO_MAIN_PAGE_MARKUP = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) \
    .add(telebot.types.KeyboardButton('↩ Вернуться'))
