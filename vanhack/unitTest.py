import unittest
from vanhack.book_Stock import in_stock


class Test(unittest.TestCase):
    def test_basic_in_stock_queries(self):
        """ basic in stock queries """
        self.assertTrue(
            in_stock("While You Were Mine", "Historical Fiction"),
            '"While You Were Mine" is available in "Historical Fiction"'
        )
        self.assertTrue(
            in_stock("Online Marketing for Busy Authors: A Step-By-Step guide", "Self help"),
            '"Online Marketing for Busy Authors: A Step-By-Step guide" is available in "Self help"'
        )
        self.assertTrue(
            in_stock("The MooSEwood Cookbook: Recipes from Moosewood Restaurant, Ithaca, New York", "food and driNk"),
            '"The MooSEwood Cookbook: Recipes from Moosewood Restaurant, Ithaca, New York" is available in "food and driNk"'
        )

    def test_basic_out_of_stock_queries(self):
        """ basic out of stock queries """
        self.assertFalse(
            in_stock("While You Were Mine", "Science"),
            '"While You Were Mine" is not available in "Science"'
        )
        self.assertFalse(
            in_stock("Online Marketing for Busy Authors: Step-By-Step guide", "Self help"),
            '"Online Marketing for Busy Authors: Step-By-Step guide" is not available in "Self help"'
        )