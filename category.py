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
        difficulties = ["easy", "medium", "hard"]
        point_value = 100
        for difficulty in difficulties:
            question_json = api_request.get_questions_for_specific_category_by_difficulty(self.name, difficulty)
            questions.append(Question(question_json[0], point_value))
            point_value += 100
            if difficulty != "easy":
                questions.append(Question(question_json[1], point_value))
                point_value += 100

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

