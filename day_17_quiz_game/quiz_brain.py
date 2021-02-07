# TODO: Define QuizBrain class
# TODO: Add functionality to ask questions
# TODO: Add functionality to check answers
# TODO: Add functionality to check if we are at the end of the question set


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.response = False
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        self.response = input(f" Q.{self.question_number}: {question.text} (True/False)?")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_reponse(self):
        question = self.question_list[self.question_number - 1]
        if self.response.lower() == question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def print_score(self):
        print("You've completed the quiz.")
        print(f"Your final score was {self.score}/{len(self.question_list)}.")