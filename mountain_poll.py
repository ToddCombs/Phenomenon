# author:ToddCombs
# 使用用户输入来填充字典
def exercise_21():

    responses = {}
    # 设置标识指出调查是否继续
    polling_active = True

    while polling_active:
        # 提示用户输入名字和回答
        name = input("\nWhat is your name?")
        response = input("Which mountain would you like to climb someday?")
        # 将答案存储到字典中
        responses[name] = response
        # 看看是否有人想参与调查
        repeat = input("Would you like to let another person respond? (yes/ no) " )
        if repeat == 'no':
            polling_active = False

    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " Would like to climb " + response + ".")

    print(responses)









exercise_21()