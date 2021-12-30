from ..database_common import connection_handler
import sys
sys.path.append("../..")
from interact.Display import Display
from interact.Input import Input
from variable_storage import string_factory as str_f


class PriceGetter:

    @staticmethod
    def get_avg_per_neighbourhood():
        neighbourhood_groups = PriceGetter.get_neighbourhood_groups()
        Display.clean_console()
        # Display all neighbourhood groups:
        Display.present_result(neighbourhood_groups, "neighbourhood_group")
        # Choose a specific group:
        chosen_group = Input.ask_for_string(str_f.ASK_FOR_NEIGHBOURHOOD)
        avg_price = PriceGetter.get_avg_price_of_group(chosen_group)
        Display.present_result(avg_price, 'average')

    @staticmethod
    @connection_handler
    def get_neighbourhood_groups(cursor):
        cursor.execute(
            "SELECT neighbourhood_group FROM neighbourhood GROUP BY neighbourhood_group;"
        )
        return cursor.fetchall()

    @staticmethod
    @connection_handler
    def get_avg_price_of_group(cursor, chosen_group):
        cursor.execute(
            f"SELECT trunc(avg(price)::numeric,2) AS average FROM listing WHERE neighbourhood_group = '{chosen_group}';"
        )
        return cursor.fetchall()
