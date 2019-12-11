# author:ToddCombs
def exercise_11():

    requested_topping = 'mushrooms'
    if requested_topping != 'anchovies':
        print("Hold the anchovies!")

    answer = 17
    if answer != 42:
        print("That is not the correct answer. Please try again!")

    # 检查特定值是否在列表内
    banned_users = ['andrew','carolina','david','todd','combs']
    user = 'marie'
    if user not in banned_users:
        print(user.title() + ", you can post a response if you wish.")

    age = 17
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you registered to vote yet?")
    else:
        print("Sorry, you are too young to vote.")
        print("Please register to vote as soon as you turn 18!")

    # if-elif-else
    age_1 = 12
    if age_1 < 4:
        print("Your admission cost is $0.")
    elif age_1 < 18:
        print("Your admission cost is $5.")
    else:
        print("Your admission cost is $10.")

    # 更简单的写法
    age_2 = 64
    if age_2 < 4:
        price = 0
    elif age_2 < 18:
        price = 5
    # 年龄不到65岁则门票价格赋值为10
    elif age_2 < 65:
        price = 10
    # 否则门票价格会赋值为5
    else:
        price = 5
    print("Your admission cost is $" + str(price) + ".")

    # 可以省略else
    age_3 = 12
    if age_3 < 4:
        price = 0
    elif age_3 < 18:
        price = 5
    elif age_3 <65:
        price = 10
    # 较上面的例子，使用一条elif比用else逻辑更清晰，条件过多时，应使用一系列elif代替else,这样只有满足特定条件才会执行代码
    elif age_3 >= 65:
        price = 5
    print("Your admission cost is $" + str(price) + ".")

    # elif 每个条件都会逐一检查，而else则会跳过余下的条件
    requested_toppings = ['mushrooms','extra cheese']
    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms.")
    elif 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
    elif 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")
    print("\nFinished making your pizza!")

    # 如果等于‘green peppers’则打印：对不起，我们现在没青椒了。
    requested_topping_1 = ['mushrooms','green peppers','extra cheese']
    for requested_toping in requested_topping_1:
        if requested_toping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding " + requested_toping + ".")
    print("\nFinished making your pizza!111111111111111")

    # 列表为空则不执行
    requested_toping_2 = []
    if requested_toping_2:
        for requested_toping2 in requested_toping_2:
            print("Adding " + requested_toping2 + ".")
        print("\nFinished making your pizza!")
    else:
        print("\n列表为空则不执行，直接执行else:Are you sure you want a plain pizza?")

    # 逐条对比两个列表字段是否一致，一致则输出列表字段，不一致则输出不一致的内容
    available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
    request_toppings = ['mushrooms','french fries','extra cheese']
    for request_topping in request_toppings:
        if request_topping in available_toppings:
            print("\nAdding " + request_topping + ".")
        else:
            print("Sooooorry, we don't have " + request_topping + ".")
    print("\nFinished making your pizza!!!!")

exercise_11()