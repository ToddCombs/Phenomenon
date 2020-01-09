# author:ToddCombs
# 导入单个类
from car import Car

my_new_car = Car('benz','c-class','2015')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()