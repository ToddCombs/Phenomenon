# author:ToddCombs
def exercise_4():
    motorcycles = ['honda','yamaha','suzuki']
    motorcycles_1 = []
    print(motorcycles)
    motorcycles[0] = 'ducati'
    print(motorcycles)
    # append()向列表添加字段，仅会在最后位添加
    motorcycles.append('dayun')
    print(motorcycles)
    motorcycles_1.append('honda')
    motorcycles_1.append('yamaha')
    print(motorcycles_1)
    # insert()向列表插入字段
    motorcycles_1.insert(0,'suzuki')
    print(motorcycles_1)
    # del()删除列表内的字段，需指定位置
    del motorcycles[0]
    print(motorcycles)
    # pop()方法在不指定位置参数的情况下默认删除列表末尾字段。如需删除列表首个字段则需pop(0)指定位置
    # 将列表删除的末尾字段存入变量中
    popped_motorcycles = motorcycles.pop()
    print(motorcycles)
    print("The last motorcycles I owned was a " + popped_motorcycles.title() + ".")
    # remove()方法用于在不清楚列表字段位置只知道字段名的情况下，指定删除列表中的字段
    motorcycles_1.remove('honda')
    print(motorcycles_1)
    # 可以将字段赋值给变量，删除列表内的字段
    motorcycles_2 = ['honda','yamaha','suzuki','dayun']
    too_expensive = 'yamaha'
    motorcycles_2.remove(too_expensive)
    print("\nA " + too_expensive.title() + " is too expensive for me.")
    print(motorcycles_2)


exercise_4()