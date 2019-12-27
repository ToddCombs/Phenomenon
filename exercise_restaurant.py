# author:ToddCombs
# 关于餐馆的类 练习题
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + ".")
        print("The restaurant is a " + self.cuisine_type.title() + " restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open!")

my_restaurant = Restaurant('toddcombs','chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('ash','french')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

