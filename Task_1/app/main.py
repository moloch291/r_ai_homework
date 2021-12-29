import sys

from variable_storage import string_factory as str_f
from interact.Input import Input
from interact.Display import Display
locate_python = sys.exec_prefix
print(locate_python)


def main():
    user_input = Input()
    Display.display_main_menu()
    user_choice = user_input.ask_for_int(str_f.MAIN_MENU_OPTIONS)
    print("User choice is: ", user_choice)


if __name__ == "__main__":
    Input.clean_console()
    main()
