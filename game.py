from player import Player
from question import Question
from api_request import get_questions_for_specific_category, get_all_categories
from random import choice

class Game:
    def __init__(self):
        self.players = []
        self.all_categories = get_all_categories()
        self.questions_per_categories = 5
        self.num_categories = 5

    def get_random_category(self) -> str:
        category = choice(self.all_categories)
        self.all_categories.remove(category)
        return category

    def add_player(self, player_name: str):
        self.players.append(Player(player_name))
