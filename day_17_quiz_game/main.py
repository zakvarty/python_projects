from question_model import Question
from data_2 import question_data
from quiz_brain import QuizBrain

# Task 1.1: write a for loop to iterate over question_data.
# Task 1.2: create a Question object from each entry in question_data
# Task 1.3: Append each Question object to the question bank

question_bank = []
for datum in question_data:
    question_text = datum["question"]
    question_answer = datum["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_reponse()
quiz.print_score()