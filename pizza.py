# author:ToddCombs
def exercise_15():
    pizza = {
        'crust':'thick',
        'toppings':['mushrooms','extra cheese','egg','shrimp','green pepper']

    }
    print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")
    for topping in pizza['toppings']:
        print("\t" + topping)

exercise_15()

# 形参前加*号让python创建一个名为toppings的空元组，并将收到的所有值都装到这个元组中
def make_pizza(*toppings):
    # 打印顾客点的所有配料
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 给print加循环语句对列表进行遍历。
# 注意：在函数定义中将接纳任意数量实参的形参放在最后。python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza_one(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("—— " + topping)

make_pizza_one(16,'pepperoni')
make_pizza_one(12,'mushrooms', 'green peppers', 'extra cheese')


