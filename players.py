# author:ToddCombs
# 列表
def exercise_8():

    players = ['charles','martina','michael','florence','eli','todd','combs']
    # 输出部分列表内元素，索引从0开始，到第3个
    print(players[0:3])
    # 索引从1开始，到第4个
    print(players[1:4])
    # 索引从1开始，到第3个
    print(players[1:3])
    # 如果没有指定第一个索引则会从列表头开始
    print(players[:4])
    # 没有指定第二个索引则输出后面全部的
    print(players[2:])
    # 输出列表最后三个元素
    print(players[-3:])
    print("Here is the first three players on my team:")
    # 循环输出列表前三个元素
    for player in players[:3]:
        print(player.title())

    my_foods = ['pizza','felafel','carrot cake']
    # 复制列表
    friend_foods = my_foods[:]
    print("My favorite foods are:")
    print(my_foods)
    print("\nMy friend's favorite foods are:")
    print(friend_foods)
    # 切片可以复制两个不完全相同的列表，如果直接使用friend_foods = my_foods，则相当于两个列表指向同一个列表，
    # append其中一个都会在另一个里添加上同样的元素，而使用friend_foods = my_foods[:]则相当于存副本，可以达到分别添加。
    my_foods.append('noodles')
    friend_foods.append('ice cream')
    print("My favorite foods are:")
    print(my_foods)
    print("\nMy friend's favorite foods are:")
    print(friend_foods)


exercise_8()