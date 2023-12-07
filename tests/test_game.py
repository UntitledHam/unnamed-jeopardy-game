import unittest
from game import Game
from category import Category
from question import Question
from player_collection import PlayerCollection
from api_request import get_all_category_names




class TestGame(unittest.TestCase):
    def test_get_random_category(self):
        game = Game()
        self.assertIs(type(game.get_random_category_name()), str)

    def test_generate_categories(self):
        game = Game()
        category_names = ["music", "history", "science", "geography", "food_and_drink"]
        game.generate_categories(category_names)
        for i in range(len(game.categories)):
            self.assertEquals(game.categories[i].name, category_names[i])

    def test_generate_random_categories(self):
        game = Game()
        random_category_names = ["random", "random", "random", "random", "random"]
        game.generate_categories(random_category_names)
        for category in game.categories:
            self.assertIs(type(category), Category)
            self.assertEquals(game.categories.count(category), 1)
            print(category.name)
        second_game = Game()
        random_category_names = ["random", "random", "music", "random", "random"]
        second_game.generate_categories(random_category_names)
        for category in second_game.categories:
            self.assertIs(type(category), Category)
            self.assertIsNot(type(category), None)
            self.assertEquals(second_game.categories.count(category), 1)
            for question in category.questions:
                self.assertIs(type(question), Question)
            print(category.name)

    def test_generate_board_html(self):
        game = Game()
        category_names = ["random", "random", "random", "random", "random"]
        game.generate_categories(category_names)

        print(game.generate_board_html())

    def test_init(self):
        game = Game()
        self.assertIs(type(game), Game)
        self.assertIs(type(game.players), PlayerCollection)
        self.assertEquals(get_all_category_names(), game.all_possible_categories)
        self.assertEquals([], game.categories)

    def test_reset(self):
        game = Game()
        category_names = ["music", "history", "science", "geography", "food_and_drink"]
        game.generate_categories(category_names)
        for i in range(len(game.categories)):
            self.assertEquals(game.categories[i].name, category_names[i])
        game.players.add_player("jeff")
        game.players.find_player_by_name("jeff").change_score(100)
        self.assertEquals(game.players.find_player_by_name("jeff").score, 100)
        game.reset()
        self.assertEquals([], game.categories)
        self.assertEquals(game.players.find_player_by_name("jeff").score, 0)


