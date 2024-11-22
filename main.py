from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo

print(logo)
print("WELCOME TO OUR QUIZ GAME ⭐")
question_bank = []
for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
question = quiz.still_has_questions()

while question:
    quiz.next_question()

print("THANKS FOR PLAYING 🙏")
print("you have completed the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")
