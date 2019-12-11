# author:ToddCombs
import random
# 随机生成3个或6个0-9的数字，福彩3D选号，组选3，组选6
def rnd_numbers():

    print("组选3号码是：")
    for number in range(3):
        print(random.randint(0,9))

    print("组选6号码是：")
    for number in range(6):
        print(random.randint(0,9))

rnd_numbers()
