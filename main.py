from data import question_data
from question_model import Question
from quiz_brain import QuizBrian

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrian(question_bank)

while quiz.still_has_questions():
    quiz.next_question()