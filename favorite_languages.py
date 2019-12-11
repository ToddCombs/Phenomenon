# author:ToddCombs
def exercise_13():

    favorite_languages = {
        'jen':['python','ruby'],
        'sarah':['c'],
        'edward':['ruby','php'],
        'phil':['python','java'],
        'todd':['python','java'],
        'combs':['php','go']
    }
    for name, languages in favorite_languages.items():
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())


    print("\nSarah's favorite language is " + str(favorite_languages['sarah']) + ".")

    user_0 = {
        'username':'efermi',
        'first':'enrico',
        'last':'fermi',
    }
    # 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组，声明两个变量两条print语句打印键值对。
    for key,value in user_0.items():
        print("\nKey: " + key)
        print("value: " + value)
    # 两个变量用以遍历字典内的所有items，一条语句打印键值对
    for name,language in favorite_languages.items():
        print(str.title(name) + "'s favorite languages are " + str(language) + ".")
    # keys()方法提取字典中所有的键，并打印出
    for names in favorite_languages.keys():
        print(names.title())

    friends = ['phil','sarah']
    for name in favorite_languages.keys():
        print(name.title())
        # 如果friends列表里的名字出现在字典name 里，则打印下面的语句
        if name in friends:
            print(" Hi " + name.title() + ", I see your favorite language is " + str(favorite_languages[name]) + "!")
    # 检查如果某键值对未出现在列表内则判断打印以下
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")
    # sorted()方法可以按特定顺序返回字典内的键值对，达到排序目的
    for name in sorted(favorite_languages.keys()):
        print(name.title() + ", thank you for taking the poll.")

    print("\nThe following languages have been mentioned:")
    # values()方法可以返回字典内所有值的列表，而不包含任何键
    for languages in favorite_languages.values():
        print(str(languages))

    print("\n去重后的语言有:")
    # set()方法则可以将字典内重复的值剔除
    # for languages in set(favorite_languages.values()):
    #     print(languages)


exercise_13()