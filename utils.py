import json
import requests
from question import Question


def load_questions(json_path):
    question_objects = []
    raw_data = requests.get(json_path)
    data = json.loads(raw_data.text)

    for raw_question in data:
        question = Question(
            raw_question["q"],
            raw_question["d"],
            raw_question["a"]
        )
        question_objects.append(question)
    return question_objects


def print_statistics(questions):
    count_questions, true_questions, score = 0, 0, 0

    for question in questions:
        if question.question_asked:
            count_questions += 1
        if question.is_correct():
            true_questions += 1
            score += question.score
    return f"Отвечено правильно {true_questions} вопроса из {count_questions}\n"\
           f"Набрано баллов: {score}"








