import html

class QuizBrain:
   
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list  
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(current_question["question"])
        correct_answer = current_question["correct_answer"]
        user_answer = input(f"Q{self.question_number}: {question_text} (True/False): ")
        self.check_answer(user_answer, correct_answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Pareizi!") 
            self.score += 1
        else:
            print(f"Nepareizi! Pareizā atbilde bija: {correct_answer}")
        print(f"Jūsu pašreizējais punktu skaits: {self.score}/{self.question_number}\n")

