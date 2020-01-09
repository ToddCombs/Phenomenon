# author:ToddCombs
# 小练习程序，提示用户输入他的名字，并json.dump存到文件中
import json

def get_new_name():
    """获取新用户名"""
    user_name = input("请输入你的姓名： ")
    file_name = 'forget_me.json'
    with open(file_name, 'w') as f_obj:
        json.dump(user_name, f_obj)
    return user_name

def get_save_name():
    """获取存储在json的用户名"""
    file_name = 'forget_me.json'
    try:
        with open(file_name) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name

def forget_me():
    """调用forget_me.json"""
    user_name = get_save_name()
    if user_name:
        print("欢迎回来，" + user_name.title() + "！")
    else:
        user_name = get_new_name()
        print("当你回来的时候我们会记住你的，" + user_name.title() + "！")

forget_me()