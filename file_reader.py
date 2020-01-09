# author:ToddCombs
# 从文件中读取数据，读取整个文件
# open()函数接受一个参数即要打开的文件名，python在当前执行文件所在的目录中查找指定的文件。
# 也就是在file_reader.py执行文件所在的目录中查找要打开的文件，并且存储到as后面的变量file_object中
# 关键字with在不需要访问文件后将其关闭。如果单独使用open()则 一定 需要跟close()函数关闭文件。
# with关键字是让python确定在合适的时候自动关闭文件。
with open('pi_digits.txt') as file_object:
    # read()函数读取文件的全部内容，并将其作为字符串存储在变量contents中，通过打印变量contents的值就可以将文本内容全部显示出来。
    # 打印显示的文件末尾多出一行空行，是因为read函数到达文件末尾时返回一个空字符串，将空字符串显示出来时就是一个空行。
    # 如果需要删除多出来的空行，可在print语句中使用rstrip()函数
    contents = file_object.read()
    print(contents.rstrip())

# windows系统中在文件路径中使用反斜杠\而不是斜杠/来指定文件路径
with open('d:\dp_edu\环境.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 绝对路径打开windows中的文件，目前最简单的做法是将数据文件存储在程序文件所在的目录，要么将其存储在程序文件所在目录下的一个文件夹中。
file_path = 'd:\dp_edu\环境.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 逐行读取
file_name = 'pi_digits.txt'
with open (file_name) as file_object:
    for line in file_object:
        print(line)

# 创建一个包含文件各行内容的列表
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    # readlines()函数从中读取每一行，生成一个列表并将其存储在lines变量中
    lines = file_object.readlines()
# 在with以外依然可以使用该变量
for line in lines:
    print(line.rstrip())

# 使用文件的内容
pi_string = ''
# 用循环将各行都加入pi_string,并删除每行末尾的换行符
for line in lines:
    pi_string += line.rstrip()
# 打印这个字符串及其长度
print(pi_string)
print(len(pi_string))
