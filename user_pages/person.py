from utils.render import clear_screen_before


@clear_screen_before
def render_user_menu():
    print(' ' * 10 + 'MENU \n')
    print('1. Change pass \n')
    try:
        answer = int(input('Enter option: '))
    except Exception:
        render_user_menu()
    render_user_menu(   )

