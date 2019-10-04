from mealplanner.domain.repository_sqlite import Repository


class UomRepository(Repository):
    def __init__(self, name: str):
        super(UomRepository, self).__init__(name)
        self.__create_db__()

    def clear_tables(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DELETE FROM uom;')

        conn.commit()
        conn.close()

    def drop_db(self):
        super(UomRepository, self).drop_db()
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS uom;')

        conn.commit()
        c.close()

    def save_uom(self, name, description):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute(f"INSERT INTO uom (name, description)   "
                  f"  VALUES ('{name}', '{description}') "
                  f"  ON CONFLICT(name) DO UPDATE SET "
                  f"    name='{name}',"
                  f"    description='{description}';")
        conn.commit()
        conn.close()

    def retrieve_uoms(self):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM uom;")

    def retrieve_uom_by_name(self, name):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM uom where name = ?;", [name]).fetchone()

    def __conn__(self):
        return super(UomRepository, self).__conn__()

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()

        # Create table0
        c.execute('CREATE TABLE IF NOT EXISTS uom (uom_id integer PRIMARY KEY, name text, description );')
        c.execute('CREATE UNIQUE INDEX IF NOT EXISTS uom__name ON uom (name COLLATE NOCASE);')

        conn.commit()
        conn.close()

    def populate_units_of_measure(self):
        self.save_uom("c", "cup")
        self.save_uom("tbsp", "tablespoon")
        self.save_uom("tsp", "teaspoon")
        self.save_uom("l", "litre")
        self.save_uom("ml", "millilitre")
