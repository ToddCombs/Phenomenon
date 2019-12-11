# author:ToddCombs
def exercise_16():
    # 嵌套字典
    users = {
        'einstein':{
            'first':'albert',
            'last':'einstein',
            'location':'princeton',
        },
        'curie':{
            'first':'marie',
            'last':'curie',
            'location':'paris'
        }
    }
    # for循环打印users的外层字典信息
    for username, user_info in users.items():
        print("\nUsername: " + username)
        # 循环将内层字典的键值信息赋值给变量，并打印出变量值
        full_name = user_info['first'] + " " + user_info['last']
        location = user_info['location']
        print("\tFull name: " + full_name.title())
        print("\tLocation: " + location.title())

exercise_16()