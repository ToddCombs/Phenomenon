# author:ToddCombs
# 列表
def exercise_7():
    # range()函数创建数据列表
    for value in range(1,6):
        print(value)

    # 创建一个1到100的列表
    number = list(range(1, 101))
    print(number)
    # 打印10以内的偶数（从2开始到10，步长2）
    even_numbers = list(range(2,11,2))
    print(even_numbers)


    squares = []
    # 创建一个1-10的列表
    for value_sq in range(1,11):
        # 列表内数据均做乘方运算
        square = value_sq**2
        # 将运行结果添加到squares列表里
        squares.append(square)
    print(squares)

    digits = list(range(1,1001))
    # min函数挑出列表中最小的数据，max函数找出列表中最大的，sum函数列表内所有数据求和
    print(min(digits),max(digits),sum(digits))

    # 用更便捷一些的方式生成一个乘方列表
    squares_easy = [value**2 for value in range(1,11)]
    print(squares_easy)

    # 小练习
    for numbers in range(1,21):
        print(numbers)

    for long_numbers in range(1,2):
        long_numbers = list(range(1,101))
        print(long_numbers)

    print(min(long_numbers),max(long_numbers),sum(long_numbers))

    for j in range(1,21,2):
        print(j)


exercise_7()