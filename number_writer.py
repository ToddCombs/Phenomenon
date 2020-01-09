# author:ToddCombs
# 存储数据，使用json.dump()和json.load()
import json
def exercise_number_writer():
    """json.dump()方法接受两个实参"""

    numbers = [2, 3, 5, 7, 11, 13]
    filename = 'numbers.json'
    with open(filename, 'w') as f_obj:
        # 使用json.dump()函数将数字列表存储到文件numbers.json中
        json.dump(numbers, f_obj)

exercise_number_writer()