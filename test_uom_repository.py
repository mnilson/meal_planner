from uom_repository import UomRepository
import unittest


class TestUomRepository(unittest.TestCase):

    def setUp(self):
        self.test_repo = UomRepository('test.db')

    def tearDown(self):
        self.test_repo.drop_db()

    def test_save_uom__should_save_both_units__when_two_provided(self):
        # Arrange
        self.test_repo.save_uom("test_uom_1", "first test unit of measure")
        self.test_repo.save_uom("test_uom_2", "second test unit of measure")

        # Act
        actual = self.test_repo.retrieve_uoms()

        # Assert
        self.assertEqual(2, len(actual.fetchall()))

    def test_save_uom__should_not_save_uom_again__when_it_already_exists(self):
        # Arrange
        self.test_repo.save_uom("test_uom_1", "first test unit of measure")
        self.test_repo.save_uom("TEST_UOM_1", "first test unit of measure")

        # Act
        actual = self.test_repo.retrieve_uoms()

        # Assert
        self.assertEqual(1, len(actual.fetchall()))

    def test_save_uom__should_save_name__when_given_name(self):
        # Arrange
        name = "test_uom_1"
        self.test_repo.save_uom(name, "anon")

        # Act
        actual = self.test_repo.retrieve_uoms().fetchone()["name"]

        # Assert
        self.assertEqual(name, actual)

    def test_save_uom__should_save_description__when_given_description(self):
        # Arrange
        description = "test_uom_1"
        self.test_repo.save_uom("anon", description)

        # Act
        actual = self.test_repo.retrieve_uoms().fetchone()["description"]

        # Assert
        self.assertEqual(description, actual)


if __name__ == '__main__':
    unittest.main()
