from ..database_common import connection_handler


class PriceGetter:

    @staticmethod
    @connection_handler
    def test_query(cursor):
        cursor.execute("SELECT * FROM neighbourhood;")
        return cursor.fetchall()
