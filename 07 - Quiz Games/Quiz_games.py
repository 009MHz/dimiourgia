from Quiz_data import question_data
from Quiz_flow import Brain


class Question:
    """Data List converter to CLass object"""

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


question_bank = []
for x in question_data:
    question_text = x['question']
    answer_text = x['correct_answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)

quiz = Brain(question_bank)
quiz.next_q()

print("You've completed the quiz")
print(f"Your final score is: {quiz.point}/{quiz.question_number}")
