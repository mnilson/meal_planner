class Ingredient:
    def __init__(self, name, ingredient_id=None):
        self.name = name
        self.ingredient_id = ingredient_id

    @staticmethod
    def from_db(row):
        return Ingredient(row["name"], row["ingredient_id"])

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name