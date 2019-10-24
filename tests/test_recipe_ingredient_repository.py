from mealplanner.domain.recipe_ingredient_repository import RecipeIngredientRepository
import unittest


class TestRecipeIngredientRepository(unittest.TestCase):

    def setUp(self):
        self.test_repo = RecipeIngredientRepository('test.db')

    def tearDown(self):
        self.test_repo.drop_db()

    def test_save_recipe_ingredient__should_save_both_ingredients__when_two_provided(self):
        # Arrange
        self.test_repo.save_recipe_ingredient(1, 1, 5.5, 1)
        self.test_repo.save_recipe_ingredient(1, 2, 10.5, 1)

        # Act
        actual = self.test_repo.retrieve_recipe_ingredients(1)

        # Assert
        self.assertEqual(2, len(actual))

    def test_save_recipe_ingredient__should_update_quantity__when_row_already_exists(self):
        # Arrange
        self.test_repo.save_recipe_ingredient(1, 1, 5.5, 1)
        self.test_repo.save_recipe_ingredient(1, 1, 10.5, 1)

        # Act
        actual = self.test_repo.retrieve_recipe_ingredients(1)

        # Assert
        self.assertEqual(1, len(actual))
        self.assertEqual(10.5, actual[0].quantity)

    def test_save_recipe_ingredient__should_update_uom__when_row_already_exists(self):
        # Arrange
        self.test_repo.save_recipe_ingredient(1, 1, 5.5, 1)
        self.test_repo.save_recipe_ingredient(1, 1, 5.5, 2)

        # Act
        actual = self.test_repo.retrieve_recipe_ingredients(1)

        # Assert
        self.assertEqual(1, len(actual))
        self.assertEqual(2, actual[0].uom_id)


if __name__ == '__main__':
    unittest.main()
