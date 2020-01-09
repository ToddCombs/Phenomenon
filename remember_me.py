# author:ToddCombs
# 保存和读取用户输入生成的数据
import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并生成一个username.json文件存储它。
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def exercise_remember_me():
    """保存和读取用户输入的数据，生成一个username.json文件存储以备调用"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username.title() + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username.title() + "!")

exercise_remember_me()

