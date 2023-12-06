import unittest
from category import Category
from question import Question


class TestCategory(unittest.TestCase):
    def test_category_and_set_questions(self):
        category = Category("music")

        for question in category.questions:
            self.assertTrue(type(question) is Question)
            self.assertIsNot(question.question_text, None)
        self.assertEquals(category.questions[0].get_point_val(), 100)

    def test_get_question_by_point_value(self):
        category = Category("music")
        for i in range(100, 600, 100):
            self.assertEquals(category.get_question_by_point_val(i).get_point_val(), i)

    def test_question_done(self):
        category = Category("music")
        category.question_done(category.get_question_by_point_val(100))
        self.assertTrue(category.done_questions.__contains__(category.get_question_by_point_val(100)))
        self.assertFalse(category.done_questions.__contains__(category.get_question_by_point_val(200)))

    def test_done_point_vals(self):
        category = Category("music")
        category.question_done(category.get_question_by_point_val(100))
        self.assertTrue(category.find_done_point_vals(), [100])
        category.question_done(category.get_question_by_point_val(200))
        self.assertTrue(category.find_done_point_vals(), [100, 200])







