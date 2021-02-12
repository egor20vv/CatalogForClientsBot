import shelve
import reporter

USER_DATA_DB_NAME = 'user_data'
DEFAULT_USER_DATA = {
    'settings': 0
}


class UserNotFoundException(Exception):
    pass


def get_user(user_id: int, create_if_notfound: bool = True):
    user_str = str(user_id)
    with shelve.open(USER_DATA_DB_NAME) as db:
        if user_str in db.cache or user_str in db:
            return db.cache[user_str] if user_str in db.cache else db[user_str]
        else:
            if not create_if_notfound:
                raise UserNotFoundException(user_str)
            else:
                db[user_str] = DEFAULT_USER_DATA.copy()
                return db.cache[user_str] if user_str in db.cache.keys() else db[user_str]


def set_user(user_id: int) -> shelve.Shelf:
    user_str = str(user_id)
    with shelve.open(USER_DATA_DB_NAME) as db:
        if not (user_str in db.cache or user_str in db):
            # if not (user_id in db.cache.keys()[user_id]) and not (user_id in db.keys()):
            db[user_str] = DEFAULT_USER_DATA.copy()
            print("new user was registered '{}'".format(user_str))
        else:
            print("this '{}' user is already registered".format(user_str))

        return db.cache[user_str] if user_str in db.cache else db[user_str]


def get_settings(user_id: int, create_if_notfound: bool = False) -> dict:
    return {
        's0': get_setting_sn(user_id, 0, create_if_notfound=create_if_notfound),
        's1': get_setting_sn(user_id, 1, create_if_notfound=create_if_notfound),
        's2': get_setting_sn(user_id, 2, create_if_notfound=create_if_notfound),
        's3': get_setting_sn(user_id, 3, create_if_notfound=create_if_notfound),
        's4': get_setting_sn(user_id, 4, create_if_notfound=create_if_notfound),
    }


def get_setting_sn(user_id: int, s_value: int, create_if_notfound: bool = False) -> bool:
    with shelve.open(USER_DATA_DB_NAME) as db:
        user_data = get_user(user_id, create_if_notfound=create_if_notfound)
        settings = user_data['settings']
        byte_value = (settings & 2 ** s_value) > 0
        return byte_value


def set_setting_sn(user_id: int, s_value: int, actual_value: bool, create_if_notfound: bool = False):
    old_value = get_setting_sn(user_id, s_value, create_if_notfound)
    user_str = str(user_id)
    if old_value != actual_value:
        with shelve.open(USER_DATA_DB_NAME) as db:
            user_data = get_user(user_id, create_if_notfound=create_if_notfound)
            if user_str in db.cache:
                db.cache[user_str] = user_data
            else:
                db[user_str] = user_data
            user_data['settings'] ^= 2 ** s_value


def turn_setting_sn(user_id: int, s_value: int, create_if_notfound: bool = False) -> bool:
    user_str = str(user_id)
    with shelve.open(USER_DATA_DB_NAME) as db:
        user_data = get_user(user_id, create_if_notfound=create_if_notfound)
        user_data['settings'] ^= 2 ** s_value
        if user_str in db.cache:
            db.cache[user_str] = user_data
        else:
            db[user_str] = user_data
        return user_data['settings'] & 2 ** s_value > 0
