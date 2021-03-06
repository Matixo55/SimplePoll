import sys


def poll():
    print("Answer with yes/no or skip question by typing skip")
    user, questions = Domain.prepare_questions()
    answers = ask_questions(user, questions)
    print("Thank You for participating")
    Domain.save_answers(answers)


def ask_questions(user, questions):
    answers = []
    for index, question in enumerate(questions):
        probability = Domain.calculate_chance(index)
        if user.eligible:
            print("Probability: ", probability)
        else:
            print("Probability: 0%")
        while True:
            answer = input(question)
            if answer.lower() not in ["yes", "no", "skip"]:
                print("Correct answers: yes/no/skip")
            else:
                if answer == "yes":
                    user.eligible = False
                answers.append(answer)
                break
    return answers


def run():
    Domain.process_data(Domain.update_data)
    poll()


if __name__ == "__main__":
    path = "/".join(__file__.split("/")[:-2])
    if path not in sys.path:
        sys.path.append(path)
    from domain.domain import Domain
    run()
