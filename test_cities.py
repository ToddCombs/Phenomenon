# author:ToddCombs
# 小练习，测试函数exercise_city_country
# assertEqual(a, b)|核实a == b
# assertNotEqual(a, b)|核实a != b
# assertTrue(x)|核实x为True
# assertFalse(x)|核实x为False
# assertIn(item, list)|核实item在list中
# assertNotIn(item, list)|核实item不在list中
import unittest2
from exercise_citys_country import get_city_country
class CityCountryTestCase(unittest2.TestCase):
    """小练习测试城市名和国家名是否格式化符合标准"""
    # 第一条测试用例
    def test_city_country_name(self):
        """是否正确格式化city和country"""
        city_country = get_city_country('beijing', 'china')
        # assertEqual核实a == b
        self.assertEqual(city_country, 'Beijing, China')

if __name__ == '__main__':
    unittest2.main()