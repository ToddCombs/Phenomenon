# author:ToddCombs
# 使用任意数量的关键字实参
# 有时候需要接受任意数量的实参，但预先不知道传递给函数的是什么样的信息，
# 这种情况下，可将函数编写成能够接受任意数量的键值对，调用语句提供多少就接受多少。
def build_profile(first, last, **user_info):

    profile = {}
    # 将姓，名加入字典中
    profile['first_name'] = first
    profile['last_name'] = last
    # 遍历字典user_info中的键值对，将每一个键值对都加入到字典profile中。最后将字典profile返回给函数调用行
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')
print(user_profile)