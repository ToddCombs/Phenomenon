# author:ToddCombs

def exercise_2():

    # 注意单双引号！
    message = "One of Python's strengths is its diverse community."
    print(message)
    name = "todd"
    print("Hello " + name.title() + ", would you like to learn some Python today?")

    famous_person = "Albert Einstein"
    message_1 = " once said,'A person who never made a mistake never tried anything new.'"
    print(name.title() + message_1, '\n',famous_person.strip() + message_1)

    #对于整数int型，需要使用str()函数告诉python 将变量表示为字符串
    age = 33
    message_3 = "Happy " + str(age) + "rd birthday!"
    print(message_3,"\n")


exercise_2()