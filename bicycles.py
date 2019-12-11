# author:ToddCombs
import random_number

def exercise_3():

    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles[0].title(),'\n',bicycles[1],'\n',bicycles[3],'\n',bicycles[-1])
    message = "My first bicycles was a " + random_number.choice(bicycles).title() + "."
    print(message)


exercise_3()
