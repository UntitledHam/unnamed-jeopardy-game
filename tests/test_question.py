import unittest
from question import Question
import json


class TestQuestion(unittest.TestCase):
    def test_question(self):
        with open("test_question_json.json", 'r') as question_input_file:
            all_questions = json.load(question_input_file)
        question_one = Question(all_questions[0], 100)
        self.assertEquals(question_one.id, "64730759cf09068746f6375a")
        question_two = Question(all_questions[1], 0)
        self.assertEquals(question_two.id, "622a1c357cc59eab6f94ffcb")

    def test_is_right_answer(self):
        with open("test_question_json.json", 'r') as question_input_file:
            all_questions = json.load(question_input_file)
        question_one = Question(all_questions[0], 100)
        self.assertTrue(question_one.is_right_answer("Tony Bennett"))
        self.assertFalse(question_one.is_right_answer("Bennett Tony"))
        self.assertFalse(question_one.is_right_answer("Dean Martin"))

    def test_getters(self):
        with open("test_question_json.json", 'r') as question_input_file:
            all_questions = json.load(question_input_file)
        question_one = Question(all_questions[0], 100)
        self.assertEquals(question_one.get_point_val(), 100)
        self.assertEquals(question_one.get_id(), "64730759cf09068746f6375a")


