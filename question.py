class Question:
    def __init__(self, question_json: dict):
        self.question_json = question_json
        self.id: int = question_json["id"]
        self.correct_answer: str = question_json["correctAnswer"]
        self.incorrectAnswers: list = question_json["incorrectAnswers"]
        self.question_text: str = question_json["question"]["text"]
        self.category: str = question_json["category"]
        self.difficulty = question_json["difficulty"]