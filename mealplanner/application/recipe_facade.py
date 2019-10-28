from mealplanner.domain.direction_repository import DirectionRepository
from mealplanner.domain.ingredient_repository import IngredientRepository
from mealplanner.domain.recipe_ingredient_repository import RecipeIngredientRepository
from mealplanner.domain.recipe_repository import RecipeRepository
from mealplanner.domain.uom_repository import UomRepository


class RecipeFacade:
    def __init__(self, db):
        self.recipe_repo = RecipeRepository(db)
        self.ingredient_repo = IngredientRepository(db)
        self.direction_repo = DirectionRepository(db)
        self.uom_repo = UomRepository(db)
        self.recipe_ingredient_repo = RecipeIngredientRepository(db)


    def get_all_ingredients(self):
        return self.ingredient_repo.retrieve_ingredients()

    def get_recipe(self, name):
        recipe = self.recipe_repo.retrieve_recipe_by_name(name)
        directions = self.direction_repo.retrieve_directions_by_recipe_id(recipe.recipe_id)
        recipe.directions = directions
        recipe_ingredients = self.recipe_ingredient_repo.retrieve_recipe_ingredients(recipe.recipe_id)
        recipe.recipe_ingredients = recipe_ingredients
        ingredient_ids = set(recipe_ingredient.ingredient_id for recipe_ingredient in recipe_ingredients)
        uom_ids = set(recipe_ingredient.uom_id for recipe_ingredient in recipe_ingredients)
        ingredients = {ingredient.ingredient_id:self.ingredient_repo.retrieve_ingredient_by_id(ingredient.ingredient_id).name for ingredient in ingredient_ids}
        uoms = {uom.uom_id:self.uom_repo.retrieve_uom_by_id(uom.uom_id).name for uom in uom_ids}
        for recipe_ingredient in recipe_ingredients:
            recipe_ingredient.uom_name = uoms[recipe_ingredient.uom_id]
            recipe_ingredient.ingredient_name = ingredients[recipe_ingredient.ingredient_id]
        return recipe