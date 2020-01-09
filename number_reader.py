# author:ToddCombs
import json
def exercise_number_reader():
    """用来读取json文件的简单程序"""
    filename = 'numbers.json'
    with open(filename) as f_obj:
        # 使用json.load()函数加载存储在numbers.json中的信息
        numbers = json.load(f_obj)

    print(numbers)

exercise_number_reader()