class Question():
    def __init__(self, questions, difficulty, correct_answer):
        self.questions = questions
        self.difficulty = int(difficulty)
        self.correct_answer = correct_answer

        self.question_asked = False
        self.user_answered = None
        self.score = self.difficulty * 10


    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.score


    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.correct_answer == self.user_answered


    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.questions}\n"\
               f"Ответ: {self.difficulty}/5"


    def build_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов или
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.score} баллов"
        return f"Ответ неверный, верный ответ {self.correct_answer}"

