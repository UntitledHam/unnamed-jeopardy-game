from player_collection import PlayerCollection
from api_request import get_all_category_names
from random import choice
from category import Category
from flask import request


class Game:
    def __init__(self):
        """
        Creates a game with a playercollection
        """
        self.players = PlayerCollection()
        self.all_possible_categories = get_all_category_names()
        self.categories = []

    def reset(self):
        """
        Resets categories and players score in order to be able to play a new game
        :post: Categories is empty list, all_possible_categories is reset, and players scores are reset
        """
        self.categories = []
        self.all_possible_categories = get_all_category_names()
        self.categories = []
        self.players.reset_all_players_score()

    def get_random_category_name(self) -> str:
        """
        Gets a random category from all_possible_categories.
        :return: A random category out of all_possible_categories.
        """
        category = choice(self.all_possible_categories)
        return category

    def get_category_from_name(self, category_name):
        """
        Searches for category by name
        :param category_name: name of category to look for
        :raise ValueError: if category not found
        :return: the category
        """
        for category in self.categories:
            if category.name == category_name:
                return category

        raise ValueError("Category not found.")

    def check_if_all_questions_are_answered(self):
        """
        Checks if all 5 questions from each category are done
        :return: True if all are done, false if not
        """
        num_done_questions = 0
        for category in self.categories:
            num_done_questions += len(category.done_questions)

        if num_done_questions >= 25:
            return True
        return False

    def generate_categories(self, category_names: list):
        """
        Generates the categories to be used for the game.
        :param category_names: A list of the category names, if the value is "random" it will choose a random category.
        :post: Categories will be a list of Category objects, sorted Alphabetically. All category names will be regenerated.
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
        self.check_category_authenticity(category_names)
        self.categories.sort(key=lambda c: c.name)
        self.all_possible_categories = get_all_category_names()

    def generate_question_buttons(self, question):
        """
        Generates HTML for question buttons
        :param question: question to generate html for
        :return: html of question buttons
        """
        player_name = request.args.get("player-name", "")
        try:
            player = self.players.find_player_by_name(player_name)
        except ValueError:
            player = None
        point_value = int(request.args.get("point-value", "0"))
        category_name = request.args.get("category", "")

        if player is not None:
            letters = ["A", "B", "C", "D"]
            boxes_html = """<div class="box"><div class="container">"""
            for i in range(len(question.answers)):
                boxes_html += f"""
                        <div>
                            <p>
                                <a href="/answer-question?category={category_name}&point-value={point_value}&player={player_name}&answer={i}">
                                    {letters[i]}
                                </a>
                                <br><br><br>
                            </p>
                            </div>"""
            boxes_html += "</div></div>"

        else:
            boxes_html = """<div class="box"><div class="container">"""
            for i in range(len(self.players.alphabetical_players)):
                player_text = f"{self.players.alphabetical_players[i].name}"
                boxes_html += f"""
                                    <div>
                                        <p>
                                            <a href="/ask-question?category={category_name}&point-value={point_value}&player-name={player_text}">
                                                {player_text}
                                            </a>
                                            <br><br><br>
                                        </p>
                                        </div>"""
            boxes_html += "</div></div>"

        return boxes_html

    def generate_board_html(self) -> str:
        """
        Generates board html
        :return: board html
        """
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

    def get_question_by_category_name_and_point_value(self, category_name, point_value):
        """
        Searches for question by category name and point value
        :param category_name: category name to look for
        :param point_value: point value to look for
        :return: the question
        """
        category = None
        for the_category in self.categories:
            if the_category.name == category_name:
                category = the_category
                break
        question = category.get_question_by_point_val(point_value)

        return question

    def ask_question(self, category_name: str, point_value: int):
        """
        Generates HTML for the question being asked
        :param category_name: Category name of question
        :param point_value: Point value of question
        :return: html that asks a question
        """
        question = self.get_question_by_category_name_and_point_value(category_name, point_value)

        letters = ["A", "B", "C", "D"]
        answers_html = ""
        for i in range(len(question.answers)):
            question_text = f"{letters[i]}: {question.answers[i]}"
            answers_html += f"{question_text}<br>"

        buttons_html = self.generate_question_buttons(question)

        html = f"""
        {self.players.generate_leaderboard_html()}
        <h1>
            {question.question_text}
        </h1>
        <p>
            {answers_html}
        </p>
        {buttons_html}
       """

        return html

    def answer_question(self, category_name, point_value, player_name, answer):
        """
        Answers a question
        :param category_name: category of question
        :param point_value: point value of question
        :param player_name: player who answered
        :param answer: answer submitted
        :post: changes players score based on questions point value and if question was incorrect or not
        :return: html based on if answer was correct or incorrect
        """
        question = self.get_question_by_category_name_and_point_value(category_name, point_value)
        category = self.get_category_from_name(category_name)
        player = self.players.find_player_by_name(player_name)
        category.done_questions.append(question)
        correct_html = f"""
            <h1>Correct!</h1>
            <p>The answer was: {question.correct_answer}</p>
            <br><br>
            <a href="/board">
                Back to board.
            </a>
        """
        incorrect_html = f"""
            <h1>Incorrect!</h1>
            <p>The answer was: {question.correct_answer}</p>
            <br><br>
            <a href="/board">
                Back to board.
            </a>
        """
        if question.answers[answer] == question.correct_answer:
            player.change_score(point_value)
            return correct_html
        else:
            player.change_score(-point_value)
            return incorrect_html

    def check_category_authenticity(self, category_names):
        """
        Checks if categories are valid and if not regenerates that category,
        :post: If a category was invalid it would fix that, if not it does nothing.
        """
        for i in range(len(category_names)):
            if self.categories[i] is None or self.categories[i].questions[4] is None:
                self.categories.remove(self.categories[i])
                self.categories.append(Category(category_names[i]))

    def skip_question(self, category_name, point_value):
        """
        Skips a question
        :param category_name: The name of the category.
        :param point_value: The points the question is worth, to find it.
        :post: Adds the question to be skipped to the done questions.
        """
        question = self.get_question_by_category_name_and_point_value(category_name, point_value)
        category = self.get_category_from_name(category_name)
        category.done_questions.append(question)

