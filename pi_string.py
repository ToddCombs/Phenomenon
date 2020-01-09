# author:ToddCombs
# 包含100万位的大型文件
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52].rstrip() + "...")
print(len(pi_string))