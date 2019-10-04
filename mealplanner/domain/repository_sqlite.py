import sqlite3


class Repository:
    def __init__(self, name: str):
        self.name = name
        self.__create_db__()

    def clear_tables(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('''DELETE FROM conversion;''')

        conn.commit()
        conn.close()

    def drop_db(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS conversion;''')

        conn.commit()
        c.close()

    def __conn__(self):
        conn = sqlite3.connect(self.name)
        conn.row_factory = sqlite3.Row
        return conn

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()

        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS conversion(uom_1_id integer, uom_2_id integer, factor real);''')

        conn.commit()
        conn.close()

    def populate_metadata_tables(self):
        self.__populate_conversions__()

    def __populate_conversions__(self):
        self.__save_conversion__("l", "ml", 0.0001)

    def __save_conversion__(self, uom_1, uom_2, conversion):
        conn = self.__conn__()
        c = conn.cursor()
        uom_1_id = c.execute("SELECT id FROM uom where name = ?;", [uom_1]).fetchone()[0]
        uom_2_id = c.execute("SELECT id FROM uom where name = ?;", [uom_2]).fetchone()[0]
        c.execute(f"INSERT INTO conversion VALUES ({uom_1_id}, '{uom_2_id}', '{conversion}');")
        conn.commit()
        conn.close()

