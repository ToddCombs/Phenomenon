# author:ToddCombs
# input()函数，用户输入交互
def exercise_17():
    message = input("Tell me something, and I will repeat it back to you: ")
    print(message)

    name = input("Please enter your name: ")
    print("Hello, " + name + "!" )

    prompt = "If you tell us who you are, we can personalize the messages you see."
    prompt += "\nWhat is your first name? "
    names = input(prompt)
    print("\nHello, " + names + "!" )










exercise_17()