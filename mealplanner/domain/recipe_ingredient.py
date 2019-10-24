class RecipeIngredient:
    def __init__(self, recipe_id, ingredient_id, uom_id, quantity):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.uom_id = uom_id
        self.quantity = quantity

    @staticmethod
    def from_db(row):
        return RecipeIngredient(row["recipe_id"], row["ingredient_id"], row["uom_id"], row["quantity"])
