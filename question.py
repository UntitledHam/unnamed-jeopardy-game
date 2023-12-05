from random import shuffle

class Question:
    def __init__(self, question_json: dict, point_value):
        self.question_json = question_json
        self.id: str = question_json["id"]
        self.correct_answer: str = question_json["correctAnswer"]
        self.answers: list = question_json["incorrectAnswers"] + [self.correct_answer]
        shuffle(self.answers)
        self.question_text: str = question_json["question"]["text"]
        self.category: str = question_json["category"]
        self.difficulty = question_json["difficulty"]
        self.point_val = point_value

    def is_right_answer(self, answer: str) -> bool:
        if answer == self.correct_answer:
            return True
        return False

    def get_point_val(self):
        return self.point_val

    def get_id(self):
        return self.id

