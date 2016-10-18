def clear_screen():
    print(chr(27) + "[2J")


def clear_screen_after(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        clear_screen()
    return wrapper


def clear_screen_before(func):
    def wrapper(*args, **kwargs):
        clear_screen()
        func(*args, **kwargs)
    return wrapper


def wait_for_clicking(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        input('Click something to return menu...')
    return wrapper
