from question_bank import question_data
from Questionmodel import Question
from brain import QuizBrain

print("Welcome to quiz master")

question_objects = []

for item in question_data:
    question_text = item["question"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_objects.append(new_question)

quiz = QuizBrain(question_objects)
quiz.start_question()
