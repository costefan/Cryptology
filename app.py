import sys
from os.path import dirname, abspath
import os.path
from settings import (
    change_current_user,
    set_cryptor,
    get_cryptor
)
from getpass import getpass
from user import User
from user_pages import render_user_menu
from utils import (
    clear_screen_before, wait_for_clicking
)
from checker import check_system_info
from cryptor import RDSCryptor


@clear_screen_before
def render_login():
    name = input('Enter your name: ')
    password = getpass('Enter your pass: ')
    if User.authenticate(name, password):
        cur_user = User(name, password)
        print(cur_user.blocked)
        print(cur_user.name)
        if cur_user.blocked:
            input('Your account was blocked')
            render_menu()
        change_current_user(cur_user)
        render_user_menu()

    else:
        render_menu()


@wait_for_clicking
@clear_screen_before
def render_information():
    print('Hi, Author of the first lab is Ovchynnikov Kostiantyn! \n'
          'SoftServe Python Engineer and KPI student \n'
          'The task was all symbols should be unique \n'
          'Click something to return menu...')


@clear_screen_before
def render_menu():
    print(' ' * 10 + 'MENU \n'
          '1. Login \n'
          '2. Information \n'
          '3. Exit \n')
    try:
        answer = int(input('Enter option: '))
    except Exception:
        render_menu()
    if answer == 1:
        render_login()
    elif answer == 2:
        render_information()
    elif answer == 3:
        print(get_cryptor())
        sys.exit()
    else:
        render_menu()


def main():
    root = dirname(abspath(__file__))
    sys.path.append(root)
    render_menu()

if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        # running in a bundle
        check_system_info()
        # encrypt users file

    path = os.path.abspath('.') + '/app'
    cryptor = RDSCryptor(path)
    cryptor.decrypt_file()
    set_cryptor(cryptor)
    main()
