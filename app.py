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
        if cur_user.blocked:
            input('Your account was blocked')
            render_menu()
        change_current_user(cur_user)
        render_user_menu()
    else:
        input('There is no user with this name')
        render_menu()


@wait_for_clicking
@clear_screen_before
def render_information():
    print('Hi, Author of the first lab is Ovchynnikov Kostiantyn! \n'
          'SoftServe Python Engineer and KPI student \n'
          'The task was all symbols should be unique \n')


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
    except BaseException:
        get_cryptor().encrypt_file()
        sys.exit()
    if answer == 1:
        render_login()
    elif answer == 2:
        render_information()
        render_menu()
    elif answer == 3:
        get_cryptor().encrypt_file()
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
