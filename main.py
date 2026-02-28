# Quiz Game Application

def run_quiz():
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "2. Which language is used for web development?",
            "options": ["A. Python", "B. C++", "C. HTML", "D. Java"],
            "answer": "C"
        },
        {
            "question": "3. Who is known as the Father of Computers?",
            "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Elon Musk"],
            "answer": "A"
        },
        {
            "question": "4. What does CPU stand for?",
            "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Power Unit"],
            "answer": "B"
        },
        {
            "question": "5. Which data structure uses FIFO?",
            "options": ["A. Stack", "B. Tree", "C. Queue", "D. Graph"],
            "answer": "C"
        }
    ]

    score = 0

    print("🎯 Welcome to the Quiz Game!")
    print("-----------------------------------")

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")

    print("\n-----------------------------------")
    print(f"🎉 Quiz Completed! Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"📊 Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("🏆 Excellent Performance!")
    elif percentage >= 50:
        print("👍 Good Job!")
    else:
        print("📘 Keep Practicing!")

if __name__ == "__main__":
    run_quiz()
