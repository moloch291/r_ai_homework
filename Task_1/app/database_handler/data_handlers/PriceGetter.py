from ..database_common import connection_handler


class PriceGetter:

    @staticmethod
    @connection_handler
    def test_query(cursor):
        query = "SELECT * FROM neighbourhood;"
        cursor.execute(query)
        return cursor.fetchall()
