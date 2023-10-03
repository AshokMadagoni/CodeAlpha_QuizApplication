class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question.question}")
            for j, option in enumerate(question.options, start=1):
                print(f"{j}. {option}")

            user_answer = int(input("Enter the number of your answer: "))
            if 1 <= user_answer <= len(question.options):
                if question.is_correct(user_answer):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is {question.correct_answer}: {question.options[question.correct_answer - 1]}\n")
            else:
                print("Invalid choice. Skipping this question.\n")

        print(f"You scored {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    # Define your questions here
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Berlin"], 1),
        Question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus"], 1),
        Question("What is 7 x 8?", ["42", "54", "56"], 3),
    ]

    quiz = Quiz(questions)
    quiz.start_quiz()
