from random import shuffle


class Question:
    def __init__(self, question_json: dict, point_value: int):
        """
        Creates question object using question_json and point value
        :param question_json: json dict with many variables
        :param point_value: point value of the question
        """
        self.id: str = question_json["id"]
        self.correct_answer: str = question_json["correctAnswer"]
        self.answers: list = question_json["incorrectAnswers"] + [self.correct_answer]
        shuffle(self.answers)
        self.question_text: str = question_json["question"]["text"]
        self.difficulty = question_json["difficulty"]
        self.point_val = point_value

    def is_right_answer(self, answer: str) -> bool:
        """
        Checks to see if an answer is correct
        :param answer: answer to check
        :return: true if answer is correct, false if incorrect
        """
        if answer == self.correct_answer:
            return True
        return False

    def get_point_val(self) -> int:
        """
        Returns point_value
        :return: point_val
        """
        return self.point_val

    def get_id(self) -> str:
        """
        Returns id
        :return: id
        """
        return self.id

