# author:ToddCombs
# 处理FileNotFoundError异常
def exercise_FileNotFoundError(filename):
    """计算一个文件大致有多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
        print(contents)
    except FileNotFoundError:
        # pass语句可以让程序出现异常时继续执行，不告诉用户。
        # pass
        msg = "Sorry, the file 【" + filename + "】 does not exist."
        print(msg)
    else:
        # 分析文本。
        # 计算文件大致包含多少单词，split方法对字符串进行切片
        words = contents.split()
        num_words = len(words)
        print("The file 【" + filename + "】 has about 【" + str(num_words) + "】 words.")
# 可以将txt文件存储在列表里
filenames = ['alice1.txt','siddhartha.txt']
# 循环调用方法判断列表内的文件是否存在，文件存在则打印文本并输出文件包含多少个字符，不存在则抛出异常。
for filename in filenames:
    exercise_FileNotFoundError(filename)
