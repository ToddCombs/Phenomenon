# author:ToddCombs
# 元组
def exercise_9():

    dimensions = (200, 50)
    print(dimensions[0])
    print(dimensions[1])

    # 循环遍历元组中所有值
    for dimension in dimensions:
        print(dimension)
    # 元组不可以被修改可以重新赋值
    dimensions = (200, 50)
    print("Original dimensions:")
    for dimension in dimensions:
        print(dimension)
    dimensions = (400,100)
    print("\nModified dimensions:")
    for dimension in dimensions:
        print(dimension)




exercise_9()