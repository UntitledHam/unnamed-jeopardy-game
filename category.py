import api_request
from question import Question

class Category:
    def __init__(self, name):
        self.name = name
        self.questions = self.set_questions()
        self.done_questions = []

    def set_questions(self):
        # Selects 5 random questions to add to the category: 1 easy, 2 med, 2 hard, with varying point vals
        questions = []
        ten_easy = api_request.get_questions_for_specific_category_by_difficulty(self.name, "easy")
        questions.append(Question(ten_easy[0], 100))
        ten_med = api_request.get_questions_for_specific_category_by_difficulty(self.name, "medium")
        questions.append(Question(ten_med[0], 200))
        questions.append(Question(ten_med[1], 300))
        ten_hard = api_request.get_questions_for_specific_category_by_difficulty(self.name, "hard")
        questions.append(Question(ten_hard[0], 400))
        questions.append(Question(ten_hard[1], 500))
        return questions

    def get_question_by_point_val(self, point_val):
        ### returns questions based on point value, returns valerror if no question is found
        if 100 >= point_val >= 500 and point_val % 100 == 0:
            for question in self.questions:
                if question.get_point_val() == point_val:
                    return question
        else:
            return ValueError("point val doesnt exist in any questions")

    def find_done_point_vals(self):
        ### returns list of point vals that are in self.done_questions
        done_point_vals = []
        for question in self.done_questions:
            done_point_vals.append(question.get_point_val())

    def question_done(self, given_question):
        for question in self.questions:
            if question.get_id() == given_question.get_id():
                self.done_questions.append(question)
                break


