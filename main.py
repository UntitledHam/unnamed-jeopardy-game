from api_request import get_questions_of_specific_category, get_all_categories
from question import Question
from player import Player
from random import choice


def main():
    player = Player("Jeff")
    categories = get_all_categories()
    while player.score >= 0:
        category = choice(categories)
        ask_question(player, category, cheatmode=True)
        clear_console()


def ask_question(player: Player, category: str, **kwargs):
    is_cheat_mode = kwargs.get("cheatmode", False)
    question_json = get_questions_of_specific_category(category)
    the_question = Question(question_json[0])
    text = f"{the_question.question_text}\nWorth: {the_question.get_point_value()} points.\nPoints: {player.score}\n\n"
    letters = ["A", "B", "C", "D"]
    for i in range(len(the_question.answers)):
        if is_cheat_mode and the_question.answers[i] == the_question.correct_answer:
            text += f"\033[92m{letters[i]}: {the_question.answers[i]}\033[00m\n"
            continue
        text += f"{letters[i]}: {the_question.answers[i]}\n"
    print(text)
    answer = input("Please enter your answer: ")
    index = letters.index(answer.upper())
    if the_question.answers[index] == the_question.correct_answer:
        player.score += the_question.get_point_value()
        print("Correct!")
    else:
        player.score -= the_question.get_point_value()
        print(f"Incorrect, the correct answer was {the_question.correct_answer}.")


def clear_console():
    print("\033[H\033[J", end="")


main()
