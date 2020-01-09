# author:ToddCombs
# 创建并写入内容到空文件
def write_message(name,msg):

    file_path = "C:\\Users\\Administrator\\PycharmProjects\\untitled1\\"
    full_path = file_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)

write_message('my_write_test','Hello world!\r\n')

file_name = 'my_write_test_1.txt'
# with open(file_name, 'w') as file_object:
# 'w'是重写，'a'是追加附加到文本后面，打开文件时指定了实参'a'以便将内容附加到文件末尾而不是覆盖原来的内容。
with open(file_name, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
