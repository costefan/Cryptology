import sys
from getpass import getpass
from utils.render import (
    clear_screen_before, wait_for_clicking
)
from settings import get_current_user, change_current_user
from .admin import (
    render_users_list, render_adding_user,
    render_block_user, render_add_limitations
)
from user import User
from settings import get_cryptor


@wait_for_clicking
def render_change_pass():
    print('You want to change password')
    old_pass = str(getpass('Enter old password: '))
    if User.check_correct_password(old_pass):
        new_pass = str(getpass('Enter new password: '))
        new_pass_copy = str(getpass('Enter new password again: '))
        if new_pass == new_pass_copy:
            new_cur_user = User.change_user(
                name=get_current_user().name, new_password=new_pass)
            change_current_user(new_cur_user)
        else:
            print('There was a mistake...You have limitations to your pass'
                  ' (all symbols should be unique)\n'
                  ' You want: \n'
                  ' 1. Try again \n'
                  ' 2. Back to menu \n'
                  ' 3. Exit')
            answer = int(input())
            if answer == 1:
                render_change_pass()
            elif answer == 2:
                render_user_menu()
            elif answer == 3:
                get_cryptor().encrypt_file()
                sys.exit()
            render_user_menu()
    else:
        print('There is limitation to your password'
              ' You want: \n'
              ' 1. Try again \n'
              ' 2. Back to menu \n'
              ' 3. Exit')
        answer = int(input())
        if answer == 1:
            render_change_pass()
        elif answer == 2:
            render_user_menu()
        elif answer == 3:
            sys.exit()
        render_user_menu()


@clear_screen_before
def render_user_menu():
    if get_current_user().is_admin:
        print(' ' * 10 + 'MENU \n'
              ' 1. Change pass \n'
              ' 2. Users list \n'
              ' 3. Add user \n'
              ' 4. Block user \n'
              ' 5. Add limitation \n'
              ' 6. Exit \n')

        try:
            answer = int(input('Enter option: '))
        except Exception:
            render_user_menu()
        if answer == 1:
            render_change_pass()
        elif answer == 2:
            render_users_list()
        elif answer == 3:
            render_adding_user()
        elif answer == 4:
            render_block_user()
        elif answer == 5:
            render_add_limitations()
        elif answer == 6:
            get_cryptor().encrypt_file()
            sys.exit()
    else:
        print(' ' * 10 + 'MENU \n'
              '1. Change pass \n'
              '2. Exit \n')

        try:
            answer = int(input('Enter option: '))
        except Exception:
            render_user_menu()
        if answer == 1:
            render_change_pass()
        elif answer == 2:
            get_cryptor().encrypt_file()
            sys.exit()

    render_user_menu()
