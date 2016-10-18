USERS_FILE = './app/credentials.txt'
ADMIN_NAME = 'ADMIN'
ADMIN_PASS = 'pas3'


def change_current_user(obj):
    global cur_user
    cur_user = obj


def get_current_user():
    global cur_user
    return cur_user


def set_cryptor(obj):
    global cryptor
    cryptor = obj


def get_cryptor():
    global cryptor
    return cryptor
