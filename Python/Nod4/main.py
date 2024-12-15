from data import fetch_data 
from quiz_game import QuizBrain 

if __name__ == "__main__":
    
    raw_questions = fetch_data() 
    questions = [
        {"question": item["question"], "correct_answer": item["correct_answer"]}
        for item in raw_questions
    ]

    quiz = QuizBrain(questions)

    while quiz.question_number < len(quiz.question_list):
        quiz.next_question()

    print("Viktorīna pabeigta")  
    print(f"Jūsu gala punktu skaits: {quiz.score}/{quiz.question_number}")
