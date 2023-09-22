#constants
CORRECT_ANSWER_INCREMENT  = 2
WRONG_ANSWER_DECREMENT = 1


class QuizBrain:
    def __init__(self):
        self.points = 0
        self.user_answer = ''
        self.answer_right_or_not = True

    def next_question(self,to_be_printed): #prints the next question
        self.user_answer = input(to_be_printed)

    def check_answer(self,answer_given_by_user,correct_answer): #checks answer inputted by user
        if answer_given_by_user.lower() == correct_answer.lower():
            self.answer_right_or_not = True #if THIS is true, then it triggers correct answer output of display_score function
            self.points+= CORRECT_ANSWER_INCREMENT
            self.display_score(correct_answer)
        else:
            self.answer_right_or_not = False #if THIS is false, then it triggers wrong answer output of display_score function
            self.points -= WRONG_ANSWER_DECREMENT
            self.display_score(correct_answer)

    def display_score(self,correct_answer):
        if self.answer_right_or_not == True:
            print("\nCORRECT ANSWER! Current score:", self.points, "\n")
        else:
            print("\nWRONG ANSWER! Correct answer was: ", correct_answer, ". Current score: ", self.points, "\n")


    def questions_left(self, no_of_questions, curr_question_no): #terminates main while loop when questions end. also outputs final score.
        if curr_question_no == no_of_questions:
            print("GAME OVER. Final score:", self.points)
            return False
        return True
