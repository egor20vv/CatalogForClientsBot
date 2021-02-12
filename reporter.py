import telebot


def get_user_id(message: telebot.types.Message) -> str:
    return "[{}, {}]".format(message.from_user.id, message.from_user.username, )