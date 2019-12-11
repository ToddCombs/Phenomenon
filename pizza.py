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