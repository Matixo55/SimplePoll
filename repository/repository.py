class Repository:
    import os.path
    global surveys, question_file
    path = os.path.dirname(__file__) + r'.\data'
    try:
        surveys = open(path + r"\first_survey.csv", "a+")
        surveys.seek(62)
        question_file = open(path + r"\questions.txt", "r")
    except FileNotFoundError:
        raise FileNotFoundError("Couldn't find file")

    @staticmethod
    def read_database():
        polls = surveys.readlines()
        for entry in polls:
            entry = entry[:-1]
            line = entry.split(",")
            yield line

    @staticmethod
    def read_questions():
        questions = []
        for line in question_file.readlines():
            questions.append(line[:-1])
        return questions

    @staticmethod
    def write_to_database(answers):
        surveys.write("{},{},{},{},{}\n".format(answers[0], answers[1], answers[2], answers[3], answers[4]))
        surveys.close()
