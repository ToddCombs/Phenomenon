# author:ToddCombs
# 名字有两个字有三个字的情况，因此函数形参需要指定其中一个名字为空字符串
def get_formatted_name(first_name, last_name, middle_name =''):

    # 检查是否传入了middle_name，如果middle_name为True则full_name为三个字否则为两个字
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
# 函数调用输入实参时返回值需要存储到一个变量中
musician = get_formatted_name('todd','combs')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)