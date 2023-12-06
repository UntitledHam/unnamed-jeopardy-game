class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def change_score(self, value):
        self.score += value