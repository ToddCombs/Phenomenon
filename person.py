# author:ToddCombs
# 返回一个字典，其中包含有关一个人的信息
def build_person(first_name,last_name,age=''):
    # 将传入的实参存入字典
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    # 返回表示人的整个字典
    return person

musician = build_person('todd','combs',age=33)
print(musician)


def get_formatted_name(f_name,l_name):

    full_name = f_name + ' ' + l_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")
    # 无限循环的情况最好加break。每次调用该函数，就执行一次
    break

# 判断用户如果输入q则跳出函数
while True:
    print("\nPlease tell me your name2:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")


def city_country(city_name,city_country):

    city_dict = {'city':city_name,'country':city_country}
    return city_dict

city = city_country('Beijing','China')
print(city)
city = city_country('NewYork','America')
print(city)
city = city_country('Moscow','Russia')
print(city)
