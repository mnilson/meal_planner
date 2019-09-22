from ingredient_repository import IngredientRepository
import unittest


class TestIngredientRepository(unittest.TestCase):

    def setUp(self):
        self.test_repo = IngredientRepository('test.db')

    def tearDown(self):
        self.test_repo.drop_db()

    def test_save_ingredient__should_save_both_units__when_two_provided(self):
        # Arrange
        self.test_repo.save_ingredient("test_ingredient_1")
        self.test_repo.save_ingredient("test_ingredient_2")

        # Act
        actual = self.test_repo.retrieve_ingredients()

        # Assert
        self.assertEqual(2, len(actual.fetchall()))

    def test_save_ingredient__should_not_save_ingredient_again__when_it_already_exists(self):
        # Arrange
        self.test_repo.save_ingredient("test_ingredient_1")
        self.test_repo.save_ingredient("test_ingredient_1")

        # Act
        actual = self.test_repo.retrieve_ingredients()

        # Assert
        self.assertEqual(1, len(actual.fetchall()))

    def test_save_ingredient__should_save_name__when_given_name(self):
        # Arrange
        name = "test_ingredient_1"
        self.test_repo.save_ingredient(name)

        # Act
        actual = self.test_repo.retrieve_ingredients().fetchone()["name"]

        # Assert
        self.assertEqual(name, actual)


if __name__ == '__main__':
    unittest.main()
