# author:ToddCombs
# 使用类和实例，下面是关于汽车的类。包括给属性指定默认值，修改属性的值。
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

# 根据Car类创建了一个实例，并将其存储到变量my_new_car中
my_new_car = Car('benz', 'c-class', 2015)
# 调用get_descriptive_name方法支出我们有一辆什么样的汽车
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 修改属性的值最简单的办法是通过实例直接访问，直接将里程表读书设置为23
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 通过方法修改属性的值，且不能低于23
my_new_car.update_odometer(23)
my_new_car.read_odometer()
# 创建一辆新的二手车
my_used_car = Car('benz','amg-c63',2025)
print(my_used_car.get_descriptive_name())
# 将二手车里程表数值设置为23500
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
# 传入100增加从购买到登记期间行驶的100英里
my_used_car.increment_odometer(100)
my_used_car.read_odometer()