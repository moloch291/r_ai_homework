import sys
import time
from variable_storage import string_factory as str_f
from interact.Input import Input
from interact.Display import Display
from database_handler.data_handlers.PriceGetter import PriceGetter


def exit_program():
    print(str_f.GOOD_BYE_MESSAGE)
    time.sleep(1)
    sys.exit(0)


def reload():
    enter = Input.ask_for_string(str_f.ASK_FOR_ENTER)
    if enter == "":
        main()
    reload()


def evaluate(user_choice):
    switch = {
        1: PriceGetter.get_avg_per_neighbourhood(),
        2: 'Another result...',
        3: 'Another result...',
        4: 'And another....',
        5: 'Exit'
    }
    return switch.get(user_choice, "Invalid choice!")


def main():
    # Choosing functionality:
    Display.display_main_menu()
    user_choice = Input.ask_for_int(str_f.MAIN_MENU_OPTIONS)
    # Obtaining and presenting the data:
    evaluate(user_choice)
    reload()


if __name__ == "__main__":
    Display.clean_console()
    main()
