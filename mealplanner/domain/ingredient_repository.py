from mealplanner.domain.repository_sqlite import Repository
from mealplanner.domain.ingredient import Ingredient

class IngredientRepository(Repository):
    def __init__(self, name: str):
        super(IngredientRepository, self).__init__(name)
        self.__create_db__()

    def clear_tables(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DELETE FROM ingredient;')

        conn.commit()
        conn.close()

    def drop_db(self):
        super(IngredientRepository, self).drop_db()
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS ingredient;')

        conn.commit()
        c.close()

    def save_ingredient_2(self, ingredient):
        conn = self.__conn__()
        c = conn.cursor()
        if ingredient.ingredient_id is None:
            query = f"INSERT INTO ingredient (name) VALUES('{ingredient.name}') "
            ingredient.ingredient_id = c.execute(query).lastrowid
        else:
            c.execute(f"UPDATE ingredient SET name = '{ingredient.name}' WHERE ingredient_id = {ingredient.ingredient_id} ")
        conn.commit()
        conn.close()
        return ingredient

    def retrieve_ingredients(self):
        conn = self.__conn__()
        c = conn.cursor()
        return [Ingredient.from_db(row) for row in c.execute("SELECT * FROM ingredient;")]

    def retrieve_ingredient_by_id(self, ingredient_id):
        conn = self.__conn__()
        c = conn.cursor()
        return Ingredient.from_db(c.execute("SELECT * FROM ingredient where ingredient_id = ?;", [ingredient_id]).fetchone())

    def retrieve_ingredient_by_name(self, name):
        conn = self.__conn__()
        c = conn.cursor()
        return Ingredient.from_db(c.execute("SELECT * FROM ingredient where name = ?;", [name]).fetchone())

    def __conn__(self):
        return super(IngredientRepository, self).__conn__()

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS ingredient (ingredient_id integer PRIMARY KEY, name text COLLATE NOCASE);')
        c.execute('CREATE UNIQUE INDEX IF NOT EXISTS ingredient__name ON ingredient (name COLLATE NOCASE);')
        conn.commit()
        conn.close()
