import sys
sys.path.append("..")
from variable_storage import string_factory as str_f


class Display:

    @staticmethod
    def display_main_menu():
        print(
            str_f.LOGO,
            "\n",
            str_f.MAIN_MENU_HEADER
        )
