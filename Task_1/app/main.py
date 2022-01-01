import sys
import time
from variable_storage import string_factory as str_f
from interact.Input import Input
from interact.Display import Display
from database_handler.data_handlers.PriceGetter import PriceGetter
from database_handler.data_handlers.ResponseTimeGetter import ResponseTimeGetter
from database_handler.data_handlers.CoffeeMakerGetter import CoffeeMakerGetter

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
    if user_choice == 1:
        PriceGetter.get_avg_per_neighbourhood()
    elif user_choice == 2:
        ResponseTimeGetter.get_unique_values_of_host_response_time()
    elif user_choice == 3:
        PriceGetter.get_avg_for_most_reviewed()
    elif user_choice == 4:
        CoffeeMakerGetter.count_props_with_coffee_maker()
    elif user_choice == 5:
        exit_program()


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
