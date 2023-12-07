import api_request
from question import Question



class Category:
    def __init__(self, name):
        self.name = name
        self.questions = self.set_questions()
        self.done_questions = []

    def set_questions(self):
        # Selects 5 random questions to add to the category: 1 easy, 2 med, 2 hard, with varying point vals
        # helper method
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

    def get_question_by_point_val(self, point_value):
        ### returns questions based on point value, returns valerror if no question is found

        if point_value < 100 or point_value > 500 or point_value % 100 != 0:
            raise ValueError("Point Value is Invalid")
        lowest_index = 0
        highest_index = len(self.questions) - 1
        while lowest_index <= highest_index:
            middle_index = lowest_index + (highest_index - lowest_index) // 2
            if self.questions[middle_index].point_val > point_value:
                highest_index = middle_index - 1
            elif self.questions[middle_index].point_val < point_value:
                lowest_index = middle_index + 1
            else:
                return self.questions[middle_index]
        raise ValueError("Value is not in the list.")

    def find_done_point_vals(self):
        done_point_vals = []
        for question in self.done_questions:
            done_point_vals.append(question.get_point_val())
        return done_point_vals

    def question_done(self, given_question):
        for question in self.questions:
            if question.get_id() == given_question.get_id():
                self.done_questions.append(question)
                break

    def compare(self, category_two):
        # silly underscore fiasco solved
        strip_question_one = self.name.replace("_", "")
        strip_question_two = category_two.replace("_", "")
        if strip_question_two == strip_question_one:
            return True
        return False







