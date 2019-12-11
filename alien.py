# author:ToddCombs
# 字典
def exercise_12():
    # 定义字典
    alien_0 = {'color':'green','points':5}
    print(alien_0['color'])
    print(alien_0['points'])
    # 将字典内的键值对赋值给字符串并打印
    new_points = alien_0['points']
    print("You just earned " + str(new_points) + " points!")
    # 向字典内添加新的键值对，Python不关心键值对的添加顺序，只关心键——值之间的关系
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

    # 使用字典存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义空字典
    alien_1 = {}
    alien_1['color'] = 'green'
    alien_1['points'] = 6
    print(alien_1)

    # 修改字典内的值
    print("The alien is " + alien_0['color'] + ".")
    alien_0['color'] = 'yellow'
    print("The alien is " + alien_0['color'] + ".")

    # 向字典内增加speed键值对
    alien_0['speed'] = 'medium'
    print("\nOriginal x-position: " + str(alien_0['x_position']))
    # 如果speed值等于slow则x_increment=1
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3
    # 新键值等于老键值+增量
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print("New x-position: " + str(alien_0['x_position']))

    # 删除字典的键值对，就是永久删除了
    del alien_1['points']
    print(alien_1)

exercise_12()