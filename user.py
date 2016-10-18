from settings import (
    USERS_FILE, ADMIN_NAME, ADMIN_PASS
)
import pickle


class User:

    def __init__(self, name, password, email=None):
        self.name = name
        self.password = password
        self.email = email
        if name == ADMIN_NAME:
            self.blocked = False
            self.pass_limit = False
        else:
            for user in self.get_users(with_admin=True):
                if (self.name, self.password) == (user.get('name'),
                                                  user.get('password')):
                    self.blocked = user.get('blocked')
                    self.pass_limit = user.get('pass_limit')

    @property
    def is_admin(self):
        if self.name == ADMIN_NAME:
            return True

        return False

    @staticmethod
    def create_users(users_list: list, file_path=None):
        if not file_path:
            with open(USERS_FILE, 'wb') as users_file:
                text = ''
                for user in users_list:
                    text += ' '.join(str(key) + '=' + str(value)
                                     for key, value in user.items()) + "|"
                users_file.write(text.encode())
        else:
            with open(file_path, 'wb+') as users_file:
                pickle.dump(users_list, users_file)

    @staticmethod
    def get_users(with_admin=False):
        return_list = []
        with open(USERS_FILE, 'rb') as users_file:
            data = users_file.read().decode()
            print(data.split('|'))
            for user_data in data.split('|'):
                if user_data:
                    user = {}
                    for _ in user_data.split(' '):
                        if _:
                            splitted_param = _.split('=')
                            try:
                                user[splitted_param[0]] = splitted_param[1]
                            except IndexError:
                                user[splitted_param[0]] = ''
                    if not with_admin:
                        if user.get('name') == ADMIN_NAME:
                            continue

                    return_list.append(user)
        print('LISSSSTTTTTTTTTTTTTTTTTTTTT')
        print(return_list)
        return return_list

    @staticmethod
    def authenticate(name, password):
        try:
            if (name, password) in [
                (obj.get('name'), obj.get('password'))
                for obj in User.get_users(with_admin=True)
            ]:
                return True
        except FileNotFoundError:
            if (name, password) == (ADMIN_NAME, ADMIN_PASS):
                return True

        return False

    @staticmethod
    def change_user(name, change_blocked=False,
                    change_pass_limit=False, new_password=None):
        if name not in [
            item.get('name')
            for item in User.get_users()
        ]:
            print('There is no user with this name')
            return

        new_users = []
        user_changed = None

        for item in User.get_users(with_admin=True):
            if item.get('name') == name:
                item['blocked'] = not item['blocked'] \
                    if change_blocked else item['blocked']
                item['pass_limit'] = not item['pass_limit'] \
                    if change_pass_limit else item['pass_limit']
                item['password'] = new_password \
                    if new_password else item['password']
                user_changed = item

            new_users.append(item)

        User.create_users(new_users)
        return user_changed

    @staticmethod
    def check_correct_password(new_pass):
        if len(new_pass) == len(set(new_pass)):
            return True

        return False

    def add(self):
        all_users = self.get_users(with_admin=True)
        all_users.append({
            'name': self.name,
            'password': self.password,
            'blocked': False,
            'pass_limit': False,
            'retry_pass': 0
        })
        self.create_users(all_users)
