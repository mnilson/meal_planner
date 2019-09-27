from repository_sqlite import Repository


class IngredientRepository(Repository):
    def __init__(self, name: str):
        super(IngredientRepository, self).__init__(name)
        self.__create_db__()

    def clear_tables(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('''DELETE FROM ingredient;''')

        conn.commit()
        conn.close()

    def drop_db(self):
        super(IngredientRepository, self).drop_db()
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS ingredient;''')

        conn.commit()
        c.close()

    def save_ingredient(self, name):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute(f"INSERT INTO ingredient (name) VALUES('{name}') "
                  f"ON CONFLICT(name) DO UPDATE SET name='{name}'")
        conn.commit()
        conn.close()

    def retrieve_ingredients(self):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM ingredient;")

    def retrieve_ingredient_by_name(self, name):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM ingredient where name = ?;", [name]).fetchone()

    def __conn__(self):
        return super(IngredientRepository, self).__conn__()

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()
        print(f"~~> {c.execute('SELECT sqlite_version()').fetchone()[0]}")
        c.execute('''CREATE TABLE IF NOT EXISTS ingredient (id integer, name text COLLATE NOCASE);''')
        c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS ingredient__name ON ingredient (name COLLATE NOCASE);''')
        conn.commit()
        conn.close()
