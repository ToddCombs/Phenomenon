# author:ToddCombs

def exercise_5():

    cars = ['benz','bmw','audi','toyota','subaru']
    # sort()方法主要用于对列表永久性按首字母顺序排序
    cars.sort()
    print(cars)
    # 向sort()方法传参reverse=True，实现列表反向排序
    cars.sort(reverse=True)
    print(cars,'\n')
    cars_1 = ['benz','bmw','audi','toyota','subaru']
    # sorted()方法用于临时排序，反向排序依然是向sorted()方法内传参reverse=True
    print("Here is the original list:",'\n',cars_1)
    print("Here is the sorted list:", '\n',sorted(cars_1))
    print("Here is the original list again:",'\n',cars_1)
    # reverse()方法用于永久性反转列表字段顺序
    cars_1.reverse()
    print(cars_1)
    # len()方法用于显示列表包含多少个字段
    l = len(cars_1)
    print(l)
    # 小结，发生列表索引错误时尝试把列表长度打印出来
    # 如果想知道列表是否为空，可以print(列表名[-1])打印最后一个字段，如果为空列表则会报索引错误。任何时候都好用


exercise_5()