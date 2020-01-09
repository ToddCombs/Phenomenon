# author:ToddCombs
# 小练习，本脚本为被测试函数，城市与国家函数
def get_city_country(city, country):
    """返回一个格式化规整的城市名和国家名"""
    city_country = city + ', ' + country
    return city_country.title()
