# author:ToddCombs
# 异常，处理ZeroDivisionError异常，使用异常避免崩溃
def exercise_except():

    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("You can't divide by zero!")

    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("\nSecond number: ")
        # try内写入可能导致错误的代码。依赖于try代码块成功执行的代码都放在else中。
        try:
            answer = int(first_number) / int(second_number)
        # except告诉python出现ZeroDivisionError异常时怎么办，如果代码印除0而失败则打印友好的错误信息
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            print(answer)

exercise_except()