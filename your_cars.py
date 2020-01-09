# author:ToddCombs
# 导入模块中的所有类
import car, electric_car

your_beetle = car.Car('volkswagen','beetle',2016)
print(your_beetle.get_descriptive_name())

your_tesla = electric_car.ElectricCar('tesla','roadster',2022)
print(your_tesla.get_descriptive_name())