class Player:
    def __init__(self, name: str):
        """
        Creates a player with given name
        :param name: name of player
        """
        self.name = name
        self.score = 0

    def change_score(self, value: int):
        """
        Changes score of player
        :param value: how much score to change
        :post: changed score by value
        """
        self.score += value
