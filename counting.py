# author:ToddCombs
# while循环
def exercise_18():

    current_number = 1
    # 判断current_number是否小于等于5，是则进入循环，否则跳出。
    while current_number <= 5:
        print(current_number)
        # current_number加一
        current_number += 1

    prompt = "\nTell me something, and I will repeat it back to you: "
    # +=这里是将两个字符串拼接成一个但分行打印
    prompt += "\nEnter 'quit' to end the program. "
    # 需要将变量赋值为空字符串，让while循环可供检查，while循环首次执行时需要将message和quit进行比较
    message = ""
    # 只要message的值不等于quit则继续执行循环
    while message != 'quit':
        message = input(prompt)
        # 判断如果message不等于quit则打印用户输入的内容，相等的话就不打印quit
        if message != 'quit':
            print(message)

    prompt_1 = "\nTell me something, and I will repeat it back to you1111111111: "
    prompt_1 += "\nEnter 'quit' to end the program11111111. "
    active = True
    # 只要active的值为True则继续while循环
    while active:
        message_1 = input(prompt_1)
        # 判断如果用户输入了quit则将active 赋值为False，导致跳出循环
        if message_1 == 'quit':
            active = False
        else:
            print(message_1)

    prompt_2 = "\nTell me something, and I will repeat it back to you222222222: "
    prompt_2 += "\nEnter 'quit' to end the program22222222. "
    # 逻辑更为简单清晰的写法，while True则会一直循环，直到条件满足break跳出
    while True:
        city =  input(prompt_2)
        if city == 'quit':
            break
        else:
            print("I'd love to go to " + city.title() + "!")

    current_number_1 = 0
    while current_number_1 < 10:
        current_number_1 += 1
        # 如果除2余数为0为偶数，则continue继续执行循环，跳过print(current_number_1)，如果不能被2整除时则执行print(current_number_1)
        if current_number_1 % 2 == 0:
            continue
        print(current_number_1)

exercise_18()