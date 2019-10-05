from mealplanner.application.recipe_facade import RecipeFacade
from mealplanner.domain.uom_repository import UomRepository
import unittest


class TestRecipeFacade(unittest.TestCase):

    def setUp(self):
        self.test_facade = RecipeFacade('test.db')

    def tearDown(self):
        # self.test_repo.drop_db()
        pass

    def test___should___when_(self):
        self.test_facade.test()


if __name__ == '__main__':
    unittest.main()
