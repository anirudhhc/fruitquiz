class FruitQuiz:
    def __init__(self):
        """
        Constructor for the FruitQuiz class.
        Initializes a quiz with a set of fruit-related questions and answers.
        """
        self.questions = {
            "What fruit is known as the 'king of fruits'?": "Mango",
            "Which fruit is the most popular and most consumed in the world?": "Banana",
            "What fruit is typically used to make guacamole?": "Avocado",
            "Which fruit has seeds on the outside?": "Strawberry",
            "Which citrus fruit is known for being sour?": "Lemon"
        }
        self.score = 0

    def ask_question(self, question, correct_answer):
        """Asks the user a question and checks if the answer is correct."""
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
    
    def start_quiz(self):
        """Starts the fruit quiz and asks all the questions."""
        print("Welcome to the Fruit Quiz!")
        for question, answer in self.questions.items():
            self.ask_question(question, answer)
        
        print(f"\nYour total score is: {self.score}/{len(self.questions)}")


# Example usage:
fruit_quiz = FruitQuiz()
fruit_quiz.start_quiz()