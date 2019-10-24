from mealplanner.domain.repository_sqlite import Repository


class RecipeIngredientRepository(Repository):
    def __init__(self, name: str):
        super(RecipeIngredientRepository, self).__init__(name)
        self.__create_db__()

    def clear_tables(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DELETE FROM recipe_ingredient;')

        conn.commit()
        conn.close()

    def drop_db(self):
        super(RecipeIngredientRepository, self).drop_db()
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS recipe_ingredient;')

        conn.commit()
        c.close()

    def save_recipe_ingredient(self, recipe_id, ingredient_id, quantity, uom_id):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute(f"INSERT INTO recipe_ingredient (recipe_id, ingredient_id, uom_id, quantity)   "
                  f"  VALUES ({recipe_id}, {ingredient_id}, {uom_id}, {quantity}) "
                  f"  ON CONFLICT(recipe_id, ingredient_id) DO UPDATE SET "
                  f"    uom_id={uom_id},"
                  f"    quantity={quantity};")
        conn.commit()
        conn.close()

    def retrieve_recipe_ingredients(self, recipe_id):
        conn = self.__conn__()
        c = conn.cursor()
        return c.execute(f"SELECT * FROM recipe_ingredient where recipe_id = {recipe_id};")

    def __conn__(self):
        return super(RecipeIngredientRepository, self).__conn__()

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()

        # Create table0
        c.execute('CREATE TABLE IF NOT EXISTS recipe_ingredient (recipe_id INTEGER, ingredient_id INTEGER, uom_id INTEGER, quantity REAL);')
        c.execute('CREATE UNIQUE INDEX IF NOT EXISTS recipe_ingredient__recipe_id_ingredient_id ON recipe_ingredient (recipe_id, ingredient_id);')

        conn.commit()
        conn.close()

