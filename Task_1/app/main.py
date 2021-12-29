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


def evaluate(user_choice):
    switch = {
        1: PriceGetter.test_query(),
        2: 'Another result...',
        3: 'Another result...',
        4: 'And another....',
        5: exit_program()
    }
    return switch.get(user_choice, "Invalid choice!")


def main():
    # Choosing functionality:
    Display.display_main_menu()
    user_choice = Input.ask_for_int(str_f.MAIN_MENU_OPTIONS)
    # Obtaining and presenting the data:
    result = evaluate(user_choice)
    Display.present_result(result)
    reload()


def reload():
    enter = Input.ask_for_string(str_f.ASK_FOR_ENTER)
    if enter == "":
        main()
    reload()


if __name__ == "__main__":
    Input.clean_console()
    main()
