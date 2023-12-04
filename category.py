import api_request


class Category:
    def __init__(self, name):
        self.name = name
        self.questions = []
        api_request.get_questions_for_specific_category(self.name)
        for





