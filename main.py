import json
from api_request import get_questions_of_specific_category
from question import Question


def main():
    test = get_questions_of_specific_category("music")
    with open("test.json", "w") as f:
        json.dump(test, f, indent=4)

    the_question = Question(test[0])
    text = f"{the_question.question_text}\n"
    letters = ["A", "B", "C", "D"]
    for i in range(len(the_question.answers)):
        text += f"{letters[i]}: {the_question.answers[i]}\n"
    print(text)
    answer = input("Please enter your answer: ")
    index = letters.index(answer.upper())
    if the_question.answers[index] == the_question.correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect, the correct answer was {the_question.correct_answer}.")


main()
