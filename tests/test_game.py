import unittest
from game import Game
from category import Category
from question import Question
from player_collection import PlayerCollection
from api_request import get_all_category_names




class TestGame(unittest.TestCase):
    # Running all tests at same time can return errors due to rate-limiting
    # Excludes tests that return HTML as they are tested through Flask
    def test_get_random_category(self):
        game = Game()
        self.assertIs(type(game.get_random_category_name()), str)

    def test_generate_categories(self):
        game = Game()
        category_names = ["music", "history", "science", "geography", "food_and_drink"]
        game.generate_categories(category_names)
        for name in category_names:
            self.assertTrue(category_names.__contains__(name))

    def test_generate_random_categories(self):
        game = Game()
        random_category_names = ["random", "random", "random", "random", "random"]
        game.generate_categories(random_category_names)
        for category in game.categories:
            self.assertIs(type(category), Category)
            self.assertEquals(game.categories.count(category), 1)
            print(category.name)
        second_game = Game()
        random_category_names = ["random", "random", "random", "random", "random"]
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

    def test_check_if_all_questions_are_answered(self):
        game = Game()
        game.generate_categories(["random", "random", "random", "random", "random"])
        self.assertFalse(game.check_if_all_questions_are_answered())
        for category in game.categories:
            for question in category.questions:
                category.question_done(question)
        self.assertTrue(game.check_if_all_questions_are_answered())

    def test_get_question_by_category_name_and_point_value(self):
        game = Game()
        game.generate_categories(["music", "geography", "random", "random", "random"])
        self.assertTrue(game.get_question_by_category_name_and_point_value("music", 100),
                        game.get_category_from_name("music").get_question_by_point_val(100))
        self.assertTrue(game.get_question_by_category_name_and_point_value("geography", 200),
                        game.get_category_from_name("music").get_question_by_point_val(200))

    def test_get_category_from_name(self):
        game = Game()
        category_names = ["music", "history", "science", "geography", "food_and_drink"]
        game.generate_categories(category_names)
        for i in range(5):
            self.assertTrue(game.get_category_from_name(category_names[i]), game.categories[i])