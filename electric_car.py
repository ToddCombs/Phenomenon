# author:ToddCombs
# 继承，子类的方法__init__() ,创建子类时，父类必须包含在当前文件中，且在子类前面。
class Car():
    """模拟汽车的简单例子"""
    def __init__(self,make,model,year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        # 类中的每个属性必须有初始值，哪怕值是0或空字符串
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        # 创建一个对汽车进行描述的字符串，无需分别打印每个属性的值。为了在方法中访问属性值，使用self.make的方式
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        # 返回一个大写title的值
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This is car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性，电瓶
    """
    def __init__(self,make,model,year):
        """
        初始化父类的属性
        super()是一个特殊函数，帮助父类和子类关联起来。这行代码让python调用父类方法__init__()
        让ElectricCar实例包含父类所有属性。父类也称为超类(superclass)
        """
        super().__init__(make,model,year)
        # 所有父类Car实例都不包含battery_size，而根据ElectricCar子类创建的所有实例都包含这个属性
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla','model s',2022)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

class NuclearCar(Car):
    """原子神教！核动力汽车"""
    def __init__(self,make,model,year):
        """初始化父类的属性哟"""
        super().__init__(make, model, year)

my_nuclear_car = NuclearCar('nuclear coke','model b',2073)
print(my_nuclear_car.get_descriptive_name())
