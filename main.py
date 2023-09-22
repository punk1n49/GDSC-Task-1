from quesiton_data import data
from quizbrain import QuizBrain
from question_blueprint import Question

QUESTION_LIST = []

for item in data: #loops through dictionary to make new question objects, adds them to Q list.
    new_question = Question(item['text'],item['answer'])
    QUESTION_LIST.append(new_question)

quiz_brain = QuizBrain() #creates quiz brain object


question_idx = -1   

while quiz_brain.questions_left(len(QUESTION_LIST)-1,question_idx): #main while loop that runs the game
    question_idx += 1
    quiz_brain.next_question(QUESTION_LIST[question_idx].question)
    quiz_brain.check_answer(quiz_brain.user_answer,QUESTION_LIST[question_idx].answer)


