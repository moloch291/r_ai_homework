import sys
sys.path.append("..")
from variable_storage import string_factory as str_f


class Display:

    @staticmethod
    def display_main_menu():
        print(str_f.LOGO, "\n", str_f.MAIN_MENU_HEADER)

    @staticmethod
    def present_result(result):
        print(str_f.RESULT_HEADER, "\n")
        line_number = 1
        output = ""
        for line in result:
            output += f"{str(line_number)}: {str(line)}"
            line_number += 1
        output += "\n"
        print(output)
