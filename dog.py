# author:ToddCombs
# 类，python中规定首字母大写的名称指的是类
class Dog():
    '''一次模拟小狗的简单尝试'''

    def __init__(self, name, age):
        # __init__()是一个特殊方法，每当根据Dog类创建新实例时，python都会自动运行他
        # 形参self必不可少，必须位于其他形参前面。因为python在调用__init__方法创建Dog实例时，将自动传入实参self。
        # 每个与类相关的方法调用都自动传递实参self，这是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
        # 创建Dog实例时，python调用Dog类的__init__()方法。我们通过实参向Dog()传递name和age，self会自动传递
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + " rolled over!")

# python使用实参willie和6调用Dog类中的__init__()方法。方法__init__()创建一个表示小狗的示例。我们提供的值来设置属性name,age
# 方法__init__()并未显式的包含return语句，但python自动返回一个表示这条小狗的实例。将实例存储在my_dog中
# 通常可以认为首字母大写的名称如Dog指的是类，而小写名称如my_dog指的是根据类创建的实例
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# 调用类中的方法
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


