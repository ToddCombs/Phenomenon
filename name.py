# author:ToddCombs
import this
def exercise_1():

    # title()首字母大写，upper()全大写，lower()全小写
    name = "Ada lovelace"
    print(name.title())
    print(name.upper())
    print(name.lower(), "\n")

    # 使用+拼接字符串
    first_name = "ada"
    last_name = "lovelace"
    full_name = first_name + " " + last_name
    print(full_name)
    message = "Hello, " + full_name.title() + "!"
    print(message, "\n")

    # \t输入空白    \n换行
    print("\tPython")
    print("Languages:\nPython\nC\nJavaScript", "\n")

    favorite_language = 'Python '
    favorite_language1 = ' Python'
    favorite_language2 = ' Python '
    # rstrip()临时删除尾部的空格，lstrip()临时删除首部的空格，strip()临时删除首尾空格。
    # 如需永久删除字符串的空格需要将删除操作结果存回变量中，函数常用于存储用户输入前对其清理
    print(favorite_language.rstrip())
    print(favorite_language1.lstrip())
    print(favorite_language2.strip(), '\n')


exercise_1()