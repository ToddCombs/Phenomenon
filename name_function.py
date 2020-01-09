# author:ToddCombs
# 被测试函数
# 修改被测函数使middle变为可选参数而非必要参数，并为可选参数赋默认值
def get_formatted_name(first, last, middle=''):
    """生成格式整洁的全名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()