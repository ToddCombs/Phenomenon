# author:ToddCombs
# 嵌套：将列表作为值存储到字典内，被称为嵌套。可以在列表内嵌套字典，在字典内嵌套列表，甚至在字典内嵌套字典。
def exercise_14():

    alien_0 = {'color':'green','points':5}
    alien_1 = {'color':'yellow','points':10}
    alien_2 = {'color':'red','points':15}
    alien_3 = {'color':'blue','points': 20}

    aliens = [alien_0,alien_1,alien_2,alien_3]
    for alien in aliens:
        print(alien)
    print("\n")
    # 声明一个空列表，再循环生成值
    aliens_1 = []
    for alien_number in range(30):
        new_alien = {'color':'green','points':5,'speed':'slow'}
        # 生成的new_alien值添加到aliens_1列表内
        aliens_1.append(new_alien)
    # 打印出列表aliens_1的前五个值
    for alien in aliens_1[:5]:
        print(alien)
    print("...")
    # str()以字符串形式输出，len()列表内元素的个数
    print("Total number of aliens:" + str(len(aliens_1)) + "\n")

    aliens_2 = []
    for alien_number in range(0,30):
        new_alien = {'color':'green','points':5,'speed':'slow'}
        # 每次循环，列表aliens_2都调用append将new_alien添加进列表内
        aliens_2.append(new_alien)
    # 判断如果列表内的前三个alien的'color'值如果等于'green'则赋值该alien的color,points,speed等
    for alien in aliens_2[0:4]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['points'] = 10
            alien['speed'] = 'medium'
    # 循环输出aliens_2列表内的前6个值
    for alien in aliens_2[:10]:
        print(alien)
    print("...\n")
    for alien in aliens_2[0:2]:
        if alien['color'] == 'yellow':
            alien['color'] = 'blue'
            alien['points'] = 15
            alien['speed'] = 'fast'
    for alien in aliens_2[:10]:
        print(alien)
    print(".........\n")
    








exercise_14()