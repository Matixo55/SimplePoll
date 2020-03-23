__all__ = ["Domain"]

from repository import Repository


class Chances:
    def __init__(self):
        self.all = 0
        self.correct = 0
        self.chance = 1


class User:
    def __init__(self):
        self.eligible = True
        self.answers = ["U", "U", "U", "U", "U"]


class Domain:

    @staticmethod
    def calculate_chance(current_question):
        chance = 100
        for x in range(current_question, 5):
            chance *= categories[x].chance
        return str(round(chance, 0)) + "%"

    @staticmethod
    def prepare_questions():
        return User(), Repository.read_questions()

    @staticmethod
    def process_data(data_updater):
        global categories
        categories = [Chances() for x in range(5)]
        for line in Repository.read_database():
            for x in range(5):
                data_updater(x, line)

    @staticmethod
    def save_answers():
        process_answer = {"yes": "F", "no": "T", "skip": "U"}

    @staticmethod
    def update_data(index, data):
        categories[index].all += 1
        if data[index] == "F" or data[index] == "U":
            categories[index].correct += 1
        try:
            categories[index].chance = categories[index].correct / categories[index].all
        except ZeroDivisionError:
            categories[index].chance = 0
