from player_collection import PlayerCollection
from api_request import get_questions_for_specific_category_by_difficulty, get_all_category_names
from random import choice
from category import Category


class Game:
    def __init__(self):
        self.players = PlayerCollection()
        self.all_possible_categories = get_all_category_names()
        self.categories = []
        self.questions_per_categories = 5
        self.num_categories = 5

    def get_random_category(self) -> str:
        """
        Gets a random category from all_possible_categories.
        :return: A random category out of all_possible_categories.
        """
        category = choice(self.all_possible_categories)
        return category

    def generate_categories(self, category_names: list):
        """
        Generates the categories to be used for the game.
        :param category_names: A list of the category names, if the value is "random" it will choose a random category.
        :post: Categories will be a list of Category objects.
        """
        for category_name in category_names:
            if category_name == "random":
                random_category = self.get_random_category()
                self.categories.append(Category(random_category))
                self.all_possible_categories.remove(random_category)
            else:
                self.categories.append(Category(category_name))
                self.all_possible_categories.remove(category_name)

    def generate_board_html(self) -> str:
        table_html = ""
        for i in range(len(self.categories[0].questions)):
            row_html = ""
            for category in self.categories:
                row_html += f"<th>{category.questions[i].point_val}</th>"
            table_html += f"<tr>{row_html}</tr>"
        
        return f""" <table>{table_html}</table>"""
