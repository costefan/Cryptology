from utils.render import (
    clear_screen_before, wait_for_clicking
)
from settings import get_current_user
from user import User
from getpass import getpass


@clear_screen_before
@wait_for_clicking
def render_users_list():
    print('List of all users')
    for index, user in enumerate(
        User.get_users(with_admin=False)
    ):
        print('{}. name={} blocked={} limit_pass={}'.format(
            index + 1, user.get('name'),
            user.get('blocked'), user.get('pass_limit'),
        ))


@clear_screen_before
@wait_for_clicking
def render_adding_user():
    print('Add user \n')
    username = input('Write name of user: ')
    if username not in [
        item.get('name')
        for item in User.get_users()
    ]:
        password = getpass('')
        new_user = User(name=username, password=password)
        new_user.add()
    else:
        print('Name is not unique, sorry..')


@clear_screen_before
@wait_for_clicking
def render_block_user():
    print('List of all users')
    for index, user in enumerate(
        get_current_user().get_users(with_admin=False)
    ):
        print('{}. name={} blocked={} limit_pass={}'.format(
            index + 1, user.get('name'),
            user.get('blocked'), user.get('pass_limit'),
        ))
    username = str(input('Who do you want to block/unblock? Enter name please: '))

    if User.change_user(name=username, change_blocked=True):
        print('Well done!')


@clear_screen_before
@wait_for_clicking
def render_add_limitations():
    print('List of all users')
    for index, user in enumerate(
        get_current_user().get_users()
    ):
        print('{}. name={} blocked={} limit_pass={}'.format(
            index + 1, user.get('name'),
            user.get('blocked'), user.get('pass_limit'),
        ))
    username = str(input('You want to add limitation to user?'
                         ' Enter his name please: '))

    if User.change_user(name=username, change_pass_limit=True):
        print('Well done!')
