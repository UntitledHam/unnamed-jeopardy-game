from player_collection import PlayerCollection
from api_request import get_all_category_names
from random import choice
from category import Category


class Game:
    def __init__(self):
        self.players = PlayerCollection()
        self.all_possible_categories = get_all_category_names()
        self.categories = []

    def get_random_category_name(self) -> str:
        """
        Gets a random category from all_possible_categories.
        :return: A random category out of all_possible_categories.
        """
        category = choice(self.all_possible_categories)
        return category

    def check_if_all_questions_are_answered(self):
        num_done_questions = 0
        for category in self.categories:
            num_done_questions += len(category.done_questions)

        if num_done_questions >= 25:
            return True
        return False;

    def generate_categories(self, category_names: list):
        """
        Generates the categories to be used for the game.
        :param category_names: A list of the category names, if the value is "random" it will choose a random category.
        :post: Categories will be a list of Category objects, sorted Alphabetically.
        """
        self.categories = []
        amount_of_random_categories = category_names.count("random")
        filtered_names = filter(lambda n: n != "random", category_names)
        for category_name in filtered_names:
            self.categories.append(Category(category_name))
            self.all_possible_categories.remove(category_name)

        for i in range(amount_of_random_categories):
            category_name = self.get_random_category_name()
            self.categories.append(Category(category_name))
            self.all_possible_categories.remove(category_name)
        self.all_possible_categories = get_all_category_names()

    def generate_board_html(self) -> str:
        html = """<div class="box"><div class="container">"""
        for category in self.categories:
            modified_category_name = category.name.replace("_", "<br>").title()
            html += f"""<div>{modified_category_name}</div>"""
        for i in range(len(self.categories[0].questions)):
            for category in self.categories:
                if category.questions[i] in category.done_questions:
                    link_html = "<br>"
                else:
                    link_html = f"""
                    <a href=/ask-question?category={category.questions[i].category}&point-value={str(category.questions[i].point_val)}>
                        {str(category.questions[i].point_val)}
                    </a>
                    """
                html += f"""
                <div>
                    <p>
                        {link_html}
                    </p>
                </div>"""
        return f"""{html}</div></div>"""

    def ask_question(self, category_name: str, point_value: int):
        category = None
        for the_category in self.categories:
            if the_category.name == category_name:
                category = the_category
                break
        question = category.get_question_by_point_val(point_value)
        letters = ["A", "B", "C", "D"]
        answers_html = ""
        for i in range(len(question.answers)):
            answers_html += f"{letters[i]}: {question.answers[i]}<br>"

        html = f"""
        {self.players.generate_leaderboard_html()}
        <h1>
            {question.question_text}
        </h1>
        <p>
            {answers_html}
        </p>
        """

        return html
