import os
import sys
sys.path.append("..")
from variable_storage import string_factory as str_f


class Input:

    def ask_for_int(self, message):
        try:
            return int(input(message))
        except ValueError:
            self.clean_console()
            print(str_f.TYPE_ERROR_INT_MENU)
            return self.ask_for_int(message)

    def ask_for_string(self, message):
        try:
            return str(input(message))
        except ValueError:
            self.clean_console()
            print("Please provide text input!")
            self.ask_for_string(message)

    @staticmethod
    def clean_console():
        os.system('cls' if os.name == 'nt' else 'clear')
