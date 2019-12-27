# author:ToddCombs
# 传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

# 将客户名存入一个列表中传递给形参names
usernames = ['hannah','ty','margot','todd','combs']
greet_users(usernames)