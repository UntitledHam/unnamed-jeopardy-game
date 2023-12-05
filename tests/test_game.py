import unittest
from game import Game


class TestGame(unittest.TestCase):
    def test_get_random_category(self):
        game = Game()
        self.assertIs(type(game.get_random_category_name()), str)

    def test_generate_categories(self):
        game = Game()
        category_names = ["random", "random", "random", "random", "random"]
        game.generate_categories(category_names)

        for category in game.categories:
            print(category.name)

    def test_generate_board_html(self):
        game = Game()
        category_names = ["random", "random", "random", "random", "random"]
        game.generate_categories(category_names)

        print(game.generate_board_html())

