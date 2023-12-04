import api_request
import question

class Category:
    def __init__(self, name):
        self.name = name
        self.questions = set_questions()

    def set_questions(self):
        questions = []
        ten_easy = api_request.get_questions_for_specific_category_by_difficulty(self.name, "easy")
        questions.append(Question(ten_easy[0], 100))










