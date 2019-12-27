# author:ToddCombs
# 在列表之间移动元素
def exercise_19():

    # 创建两个列表用于存储原始数据和已验证数据
    unconfirmed_users = ['alice','brian','candace']
    confirmed_users = []
    # 验证每个用户直到没有未验证用户为止
    # 将每个经过验证的列表都移动到已验证用户列表中
    while unconfirmed_users:
        # pop()函数以每次一个的方式从尾部删除未验证用户。
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)
    # 打印所有已验证的用户
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


exercise_19()
