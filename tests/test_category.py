import unittest
from category import Category
from question import Question

class TestCategory(unittest.TestCase):
    def test_category(self):
        category = Category("music")

        for question in category.questions:
            self.assertTrue(type(question) is Question)
            self.assertIsNot(question.question_text, None)

    def test_get_question_by_point_value(self):
        category = Category("music")
        for i in range(100, 600, 100):
            self.assertEquals(category.get_question_by_point_val(i).get_point_val(), i)





