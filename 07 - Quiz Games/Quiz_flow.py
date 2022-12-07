class Brain:
    """Main Quiz Flow & Mechanism"""

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.point = 0

    def proceed(self):
        last = len(self.question_list)
        return self.question_number == last

    def next_q(self):
        while not self.proceed():
            current = self.question_list[self.question_number]
            user_answer = input(f"Q.{self.question_number + 1}: {current.text} (True/False) ")
            self.answer_check(user_answer, current.answer)
            self.question_number += 1

    def answer_check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\nBINGO")
            self.point += 1
        else:
            print("Uh-Oh")
        print(f"The correct answer is: '{correct_answer.upper()}'")
        print(f"Your score is {self.point}/{self.question_number + 1}\n\n")