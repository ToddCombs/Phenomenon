# author:ToddCombs
# 列表
def exercise_6():

    magicians = ['alice','david','carolina','todd','combs']
    for magician in magicians:
        print(magician.title() + ", that is a great trick!")
        print("I can't wait to see you next trick, " + magician.title() + ".\n")
    # 没有缩进的print不在for循环体内，则不会调用循环
    print("Thank you, everyone. That is a great magic show!")


exercise_6()