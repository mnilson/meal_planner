class Recipe:
    def __init__(self, name, notes, ingredients, directions, recipe_id=None):
        self.name = name
        self.notes = notes
        self.ingredients = ingredients
        self.directions = directions
        self.recipe_id = recipe_id

    @staticmethod
    def from_db(row):
        return Recipe(row["name"], row["notes"], [], [])
