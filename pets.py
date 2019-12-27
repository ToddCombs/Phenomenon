# author:ToddCombs
# 删除包含特定值的所有列表元素
def exercise_20():

    pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)


exercise_20()

# 设定形参
def describe_pet(animal_type, pet_name):

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat','todd')
# 提供位置实参给函数调用
describe_pet(animal_type='dog', pet_name='combs')

# 给形参提供默认值，在定义函数时需要先列出没有默认值的形参，否则python不能正确解读位置实参
def describe_pet_1(pet_name, animal_type = 'rabbit'):

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 由于其中一个形参已设定默认值，函数调用时传一个参数pet_name即可
describe_pet_1(pet_name= 'jason')