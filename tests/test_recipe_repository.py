from mealplanner.domain.recipe import Recipe
from mealplanner.domain.recipe_repository import RecipeRepository
import unittest
import sqlite3


class TestRecipeRepository(unittest.TestCase):

    def setUp(self):
        self.test_repo = RecipeRepository('test.db')

    def tearDown(self):
        self.test_repo.drop_db()

    def test_save_recipe__should_save_both_recipes__when_two_provided(self):
        # Arrange
        self.test_repo.save_recipe_2(Recipe("test_recipe_1", "some notes", [], [], None))
        self.test_repo.save_recipe_2(Recipe("test_recipe_2", "some notes", [], [], None))

        # Act
        actual = self.test_repo.retrieve_recipes()

        # Assert
        self.assertEqual(2, len(actual))

    def test_save_recipe__should_not_save_recipe_again__when_it_already_exists(self):
        # Arrange
        recipe_id = self.test_repo.save_recipe_2(Recipe("test_recipe_1", "some notes", [], [], None))
        self.test_repo.save_recipe_2(Recipe("test_recipe_1", "some notes", [], [], recipe_id))

        # Act
        actual = self.test_repo.retrieve_recipes()

        # Assert
        self.assertEqual(1, len(actual))

    def test_save_recipe__should_not_save_recipe_again__when_it_already_exists_in_different_case(self):
        # Arrange
        self.test_repo.save_recipe_2(Recipe("test_recipe_1", "some notes", [], [], None))

        # Act/Assert
        self.assertRaises(sqlite3.IntegrityError, self.test_repo.save_recipe, "TEST_RECIPE_1", "SOME_NOTES", [], [], None)

    def test_save_recipe__should_save_name__when_given_name(self):
        # Arrange
        name = "test_recipe_1"
        self.test_repo.save_recipe_2(Recipe(name, "some notes", [], [], None))

        # Act
        actual = self.test_repo.retrieve_recipes()[0].name

        # Assert
        self.assertEqual(name, actual)


if __name__ == '__main__':
    unittest.main()
