# author:ToddCombs
# 在一个模块中存储多个类
from electric_car import ElectricCar

my_tesla = ElectricCar('tesla','model s',2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()