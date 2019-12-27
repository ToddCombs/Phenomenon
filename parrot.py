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

    height = input("How old are you, in inches?")
    # input仅将用户输入的数字存储为字符串格式，因此需要int()方法转换为整数格式
    height = int(height)
    if height >= 36:
        print("\nYou're tall enough to ride!")
    else:
        print("\nYou'll be able to ride when you're a little older.")

    number = input("Enter a number, and I'll tell you if it's even or odd: ")
    number = int(number)
    # 使用 % 判断两个数相除的 余数 是否为0 ，为0 则代表是偶数，相反为奇数。
    if number % 2 == 0:
        print("\nThe number " + str(number) + " is even.")
    else:
        print("\nThe number " + str(number) + " is odd.")


exercise_17()