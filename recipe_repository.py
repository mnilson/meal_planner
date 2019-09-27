from repository_sqlite import Repository


class RecipeRepository(Repository):
    def __init__(self, name: str):
        super(RecipeRepository, self).__init__(name)
        self.__create_db__()

    def clear_tables(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('''DELETE FROM recipe;''')
        c.execute('''DELETE FROM recipe_ingredient;''')

        conn.commit()
        conn.close()

    def drop_db(self):
        super(RecipeRepository, self).drop_db()
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS recipe;''')
        c.execute('''DROP TABLE IF EXISTS recipe_ingredient;''')

        conn.commit()
        c.close()

    def save_recipe(self, name, notes, ingredients, directions):
        conn = self.__conn__()
        c = conn.cursor()

        query = f"INSERT INTO recipe (name, notes) " \
                f"  VALUES ('{name}', '{notes}') " \
                f"  ON CONFLICT(name) DO UPDATE SET " \
                f"    notes='{notes}', " \
                f"    name='{name}'"
        c.execute(query)

        # insert ingredients

        # insert directions

        conn.commit()
        conn.close()

    def retrieve_recipes(self):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM recipe;")

    def retrieve_recipe_by_name(self, name):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute("SELECT * FROM recipe where name = ?;", [name]).fetchone()

    def __conn__(self):
        return super(RecipeRepository, self).__conn__()

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS recipe (name text COLLATE NOCASE, notes text);')
        c.execute('CREATE TABLE IF NOT EXISTS recipe_ingredient(recipe_id integer, quantity real, uom_id);')
        c.execute('CREATE UNIQUE INDEX IF NOT EXISTS recipe__name ON recipe (name COLLATE NOCASE);')
        conn.commit()
        conn.close()