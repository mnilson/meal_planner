from mealplanner.domain.direction_repository import DirectionRepository
from mealplanner.domain.ingredient_repository import IngredientRepository
from mealplanner.domain.recipe_repository import RecipeRepository
from mealplanner.domain.uom_repository import UomRepository


class RecipeFacade:
    def __init__(self, db):
        self.recipe_repo = RecipeRepository(db)
        self.ingredient_repo = IngredientRepository(db)
        self.direction_repo = DirectionRepository(db)
        self.uom_repo = UomRepository(db)


    def test(self):
        self.recipe_repo.retrieve_recipes()
        self.direction_repo.retrieve_directions()
        self.ingredient_repo.retrieve_ingredients()
        self.uom_repo.retrieve_uoms()
