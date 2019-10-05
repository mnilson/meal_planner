from mealplanner.domain.ingredient import Ingredient
from mealplanner.domain.ingredient_repository import IngredientRepository
import unittest
import sqlite3


class TestIngredientRepository(unittest.TestCase):

    def setUp(self):
        self.test_repo = IngredientRepository('test.db')

    def tearDown(self):
        self.test_repo.drop_db()

    def test_save_ingredient__should_save_both_ingredients__when_two_provided(self):
        # Arrange
        self.test_repo.save_ingredient_2(Ingredient("test_ingredient_1"))
        self.test_repo.save_ingredient_2(Ingredient("test_ingredient_2"))

        # Act
        actual = self.test_repo.retrieve_ingredients()

        # Assert
        self.assertEqual(2, len(actual))

    def test_save_ingredient__should_not_save_ingredient_again__when_it_already_exists(self):
        # Arrange
        ingredient = Ingredient("test_ingredient_1")
        self.test_repo.save_ingredient_2(ingredient)

        # Act
        self.assertRaises(sqlite3.IntegrityError, self.test_repo.save_ingredient_2, Ingredient("test_ingredient_1"))

    def test_save_ingredient__should_not_save_ingredient_again__when_it_already_exists_in_different_case(self):
        # Arrange
        ingredient = self.test_repo.save_ingredient_2(Ingredient("test_ingredient_1"))
        self.test_repo.save_ingredient_2(Ingredient("TEST_INGREDIENT_1", ingredient.ingredient_id))

        # Act
        actual = self.test_repo.retrieve_ingredients()

        # Assert
        self.assertEqual(1, len(actual))

    def test_save_ingredient__should_save_name__when_given_name(self):
        # Arrange
        name = "test_ingredient_1"
        self.test_repo.save_ingredient_2(Ingredient(name))

        # Act
        actual = self.test_repo.retrieve_ingredients()[0].name

        # Assert
        self.assertEqual(name, actual)


if __name__ == '__main__':
    unittest.main()
