class QuizBrian:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        usr_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?:")
        self.check_answer(usr_answer, question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz!")
            print(f'Your final score is: {self.score}/{self.question_number}')
            return False

    def check_answer(self, usr_answer, answer):
        if usr_answer.lower() == answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong :(")

        print(f"The correct answer is: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
