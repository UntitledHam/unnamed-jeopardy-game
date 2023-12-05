import unittest
from api_request import *

class TestApiRequest(unittest.TestCase):
    def test_make_request(self):
        with self.assertRaises(ValueError):
            make_request("https://the-trivia-api.com/questions")

    def test_get_all_category_names(self):
        print(get_all_category_names())




