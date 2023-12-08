import api_request
from question import Question


def make_new_questions_grouped_by_difficulty(all_questions_json):
    """
    Returns dict with lists of questions as values grouped by difficulty, made to remove excess API calls
    :param all_questions_json: all questions to sort through
    :return: a dict with difficulties as keys, and questions as values
    """
    questions_grouped_by_difficulty = {"easy": [], "medium": [], "hard": []}
    for question_json in all_questions_json:
        difficulty = question_json["difficulty"]
        match difficulty:
            case "easy":
                questions_grouped_by_difficulty["easy"].append(Question(question_json, 0))
            case "medium":
                questions_grouped_by_difficulty["medium"].append(Question(question_json, 0))
            case "hard":
                questions_grouped_by_difficulty["hard"].append(Question(question_json, 0))

    return questions_grouped_by_difficulty


class Category:
    def __init__(self, name):
        """
        Creates a category with name and set of questions
        :param name: name of category
        """
        self.name = name
        self.questions = self.set_questions()
        self.done_questions = []

    def set_questions(self):
        """
        Sets 5 questions to the category, 1 easy, 2 med, 2 hard with point values from 100-500
        :post: self.questions gets questions added to it
        """
        all_questions_json = api_request.get_questions_for_specific_category(self.name)
        grouped_questions = make_new_questions_grouped_by_difficulty(all_questions_json)
        if len(grouped_questions["easy"]) < 1:
            question_json = api_request.get_questions_for_specific_category_by_difficulty(self.name, "easy")
            grouped_questions["easy"].append(Question(question_json[0], 0))
        if len(grouped_questions["medium"]) < 2:
            question_json = api_request.get_questions_for_specific_category_by_difficulty(self.name, "medium")
            grouped_questions["medium"] += [Question(question_json[0], 0), Question(question_json[1], 0)]
        if len(grouped_questions["hard"]) < 2:
            question_json = api_request.get_questions_for_specific_category_by_difficulty(self.name, "hard")
            grouped_questions["hard"] += [Question(question_json[0], 0), Question(question_json[1], 0)]

        questions = [grouped_questions["easy"][0]] + grouped_questions["medium"][0:2] + grouped_questions["hard"][0:2]

        points = 100
        for question in questions:
            question.point_val = points
            points += 100

        return questions

    def get_question_by_point_val(self, point_value):
        """
        Searches questions to find question based off point value
        :param point_value: point value to look for
        :raise ValueError: if point value is not in the questions list, or point value is invalid
        :return: question with corresponding point value
        """
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
        """
        Returns all point values of questions that have already been done
        :return: done point values
        """
        done_point_vals = []
        for question in self.done_questions:
            done_point_vals.append(question.get_point_val())
        return done_point_vals

    def question_done(self, given_question):
        """
        Adds a question to done_questions list
        :param given_question: question to add
        :post: done_questions has an extra question
        """
        for question in self.questions:
            if question.get_id() == given_question.get_id():
                self.done_questions.append(question)
                break
