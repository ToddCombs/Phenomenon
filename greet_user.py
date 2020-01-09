# author:ToddCombs
# 与remember_me.py相关
import json
def exercise_greet_user():
    """向名字被存储在remember_me.py的用户发出问候"""
    filename = 'username.json'
    with open(filename) as f_obj:
        # 使用json.load()函数将存储在username.json中的信息读取到变量username中。
        username = json.load(f_obj)
        print("Welcome back, " + username.title() + "!")

exercise_greet_user()