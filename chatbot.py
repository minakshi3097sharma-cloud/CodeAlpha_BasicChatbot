import datetime
import random

def show_menu():
    print("\n" + "=" * 45)
    print("🤖 STUDENT ASSISTANT CHATBOT")
    print("=" * 45)
    print("You can ask me about:")
    print("1. hello / hi")
    print("2. time")
    print("3. date")
    print("4. study tips")
    print("5. motivation")
    print("6. python")
    print("7. calculator")
    print("8. exam tips")
    print("9. help")
    print("10. bye / exit")
    print("=" * 45)

def greet_user():
    print("Bot: Hello! I am your Student Assistant Chatbot.")

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"Bot: Current time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    print(f"Bot: Today's date is {current_date}")

def study_tips():
    tips = [
        "Study for 25 minutes and take a 5-minute break.",
        "Revise your notes daily.",
        "Practice coding every day.",
        "Make short notes for quick revision.",
        "Avoid distractions while studying."
    ]
    print("Bot:", random.choice(tips))

def motivation():
    quotes = [
        "Success comes from consistent practice.",
        "Believe in yourself and keep learning.",
        "Small progress every day leads to big results.",
        "Do not give up. Every expert was once a beginner.",
        "Hard work always pays off."
    ]
    print("Bot:", random.choice(quotes))

def python_info():
    print("Bot: Python is a simple, powerful, and beginner-friendly programming language.")
    print("Bot: It is used in web development, data science, AI, automation, and more.")

def calculator():
    try:
        print("\nBot: Simple Calculator")
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Bot: Result =", num1 + num2)
        elif operator == "-":
            print("Bot: Result =", num1 - num2)
        elif operator == "*":
            print("Bot: Result =", num1 * num2)
        elif operator == "/":
            if num2 == 0:
                print("Bot: Cannot divide by zero.")
            else:
                print("Bot: Result =", num1 / num2)
        else:
            print("Bot: Invalid operator.")

    except ValueError:
        print("Bot: Please enter valid numbers.")

def exam_tips():
    print("Bot: Exam Preparation Tips:")
    print("- Make a proper timetable.")
    print("- Revise important topics first.")
    print("- Practice previous year questions.")
    print("- Take short breaks while studying.")
    print("- Sleep properly before exam day.")

def help_command():
    print("Bot: You can type words like hello, time, date, study tips, motivation, python, calculator, exam tips, or bye.")

def chatbot():
    show_menu()
    name = input("Bot: What is your name? ")
    print(f"Bot: Welcome {name}! How can I help you today?")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            greet_user()

        elif user_input in ["time", "current time"]:
            tell_time()

        elif user_input in ["date", "today date", "current date"]:
            tell_date()

        elif user_input in ["study tips", "study", "tips"]:
            study_tips()

        elif user_input in ["motivation", "quote", "inspire"]:
            motivation()

        elif user_input in ["python", "python info"]:
            python_info()

        elif user_input in ["calculator", "calculate", "math"]:
            calculator()

        elif user_input in ["exam tips", "exam", "preparation"]:
            exam_tips()

        elif user_input in ["help", "menu"]:
            show_menu()
            help_command()

        elif user_input in ["bye", "exit", "quit"]:
            print(f"Bot: Goodbye {name}! Keep learning and have a great day.")
            break

        else:
            print("Bot: Sorry, I did not understand that.")
            print("Bot: Type 'help' to see what I can do.")

chatbot()
