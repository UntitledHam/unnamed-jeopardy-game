import unittest
from api_request import *
from question import Question


class TestApiRequest(unittest.TestCase):
    def test_make_request(self):
        with self.assertRaises(ValueError):
            make_request("https://the-trivia-api.com/questions")

    def test_get_all_category_names(self):
        all_category_names = get_all_category_names()
        for category_name in all_category_names:
            self.assertIs(type(category_name), str)
            print(category_name)

    def test_get_questions_for_specific_category_by_difficulty(self):
        easy_question_json = get_questions_for_specific_category_by_difficulty("music", "easy")

        easy_questions = []
        for question_json in easy_question_json:
            easy_questions.append(Question(question_json, 0))

        for question in easy_questions:
            self.assertEquals(question.difficulty, "easy")
            self.assertEquals(question.category, "music")







