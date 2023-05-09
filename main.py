import random
from constants import JSON_DATA_PATH
from utils import load_questions, print_statistics


def main():
    questions = load_questions(JSON_DATA_PATH)
    random.shuffle(questions)

    for question in questions:
        print(question.build_question())

        user_input = input("Ваш ответ: ").lower()
        question.user_answered = user_input

        question.question_asked = True

        print(question.build_feedback())

    print("\nВот и всё!")
    print(print_statistics(questions))


main()
