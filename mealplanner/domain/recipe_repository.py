from mealplanner.domain.repository_sqlite import Repository
from mealplanner.domain.recipe import Recipe


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

    def save_recipe_2(self, recipe):
        return self.save_recipe(recipe.name, recipe.notes, recipe.ingredients, recipe.directions, recipe.recipe_id)

    def save_recipe(self, name, notes, ingredients, directions, recipe_id):
        conn = self.__conn__()
        c = conn.cursor()
        if recipe_id is None:
            query = f"INSERT INTO recipe (name, notes) " \
                    f"  VALUES ('{name}', '{notes}')"
            recipe_id = c.execute(query).lastrowid
        else:
            query = f"UPDATE recipe" \
                    f"  SET " \
                    f"    notes='{notes}', " \
                    f"    name='{name}'" \
                    f"  WHERE recipe_id = {recipe_id}"
            res = c.execute(query)

        # insert ingredients
        # TODO: need recipe_ingredient object? to encapsulate ingredient and recipe specific attributes (quantity etc)

        # insert directions

        conn.commit()
        conn.close()
        return recipe_id

    def retrieve_recipes(self):
        conn = self.__conn__()
        c = conn.cursor()
        recipes = [Recipe.from_db(row) for row in c.execute("SELECT * FROM recipe;").fetchall()]
        return recipes

    def retrieve_recipe_by_name(self, name):
        conn = self.__conn__()
        c = conn.cursor()
        row = c.execute("SELECT * FROM recipe where name = ?;", [name]).fetchone()
        return Recipe(row)

    def __conn__(self):
        return super(RecipeRepository, self).__conn__()

    def __create_db__(self):
        conn = self.__conn__()
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS recipe (recipe_id integer PRIMARY KEY, name text, notes text);')
        c.execute('CREATE TABLE IF NOT EXISTS recipe_ingredient(recipe_id integer, quantity real, uom_id);')
        c.execute('CREATE UNIQUE INDEX IF NOT EXISTS recipe__name ON recipe (name COLLATE NOCASE);')
        conn.commit()
        conn.close()
