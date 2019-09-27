from direction_repository import DirectionRepository
import unittest


class TestDirectionRepository(unittest.TestCase):

    def setUp(self):
        self.test_repo = DirectionRepository('test.db')

    def tearDown(self):
        self.test_repo.drop_db()

    def test_save_direction__should_save_both_directions__when_two_provided(self):
        # Arrange
        self.test_repo.save_direction(1, "test_direction_1", 1)
        self.test_repo.save_direction(1, "test_direction_2", 2)

        # Act
        actual = self.test_repo.retrieve_directions()

        # Assert
        self.assertEqual(2, len(actual.fetchall()))

    def test_save_direction__should_not_save_direction_again__when_it_already_exists(self):
        # Arrange
        self.test_repo.save_direction(1, "test_direction_1", 1)
        self.test_repo.save_direction(1, "test_direction_1", 2)

        # Act
        actual = self.test_repo.retrieve_directions()

        # Assert
        self.assertEqual(1, len(actual.fetchall()))

    def test_save_direction__should_not_save_direction_again__when_it_already_exists_in_different_case(self):
        # Arrange
        self.test_repo.save_direction(1, "test_direction_1", 1)
        self.test_repo.save_direction(1, "TEST_DIRECTION_1", 1)

        # Act
        actual = self.test_repo.retrieve_directions()

        # Assert
        self.assertEqual(1, len(actual.fetchall()))

    def test_save_direction__should_save_direction__when_none_exist(self):
        # Arrange
        name = "test_direction_1"
        self.test_repo.save_direction(1, name, 1)

        # Act
        actual = self.test_repo.retrieve_directions().fetchone()["direction"]

        # Assert
        self.assertEqual(name, actual)


if __name__ == '__main__':
    unittest.main()
