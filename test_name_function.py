# author:ToddCombs
# 单元测试和测试用例，可通过的测试。
# 下面是一个只包含一个方法的测试用例，它检查函数get_formatted_name()在给定名和姓时能否正确地工作
# 先导入unittest2模块和要测试的函数get_formatted_name
# 断言
# assertEqual(a, b)|核实a == b
# assertNotEqual(a, b)|核实a != b
# assertTrue(x)|核实x为True
# assertFalse(x)|核实x为False
# assertIn(item, list)|核实item在list中
# assertNotIn(item, list)|核实item不在list中
import unittest2
from name_function import get_formatted_name

# 创建一个名为NameTestCase的类，用于包含一系列针对get_formatted_name()的单元测试，该类必须继承unittest2.TestCase类
class NameTestCase(unittest2.TestCase):
    """测试name_function.py"""
    # 第一条测试用例
    def test_first_last_name(self):
        """能够正确的处理像Todd Combs这样的姓名吗？"""
        # 调用get_formatted_name函数传入实参todd,combs并将返回结果存入formatted_name
        formatted_name = get_formatted_name('todd', 'combs')
        # 断言方法用来核实得到的结果是否与期望的结果一致。比较formatted_name的值与字符串'Todd Combs'是否相等，相等就pass，不等就告诉我一下。
        self.assertEqual(formatted_name, 'Todd Combs')

    # 添加新测试用例，方法名 必须 以“test_”开头，这样才会在运行test_name_function.py时自动运行
    def test_first_last_middle_name(self):
        """检查姓名中包含middle name的情况下是否能正确处理"""
        formatted_name = get_formatted_name('todd','combs','ash')
        self.assertEqual(formatted_name, 'Todd Ash Combs')

# 运行main()方法让python运行这个文件中的测试
if __name__ == '__main__':
    unittest2.main()
# 注意遇到No tests were found的
# 解决方案1，pycharm中选中要被测试的代码，选择creat New Test，直接unittest2.main或者直接删掉unittest2.main()运行脚本即可，不需要unittest2.main()
# 解决方案2，在unittest2.main()上加一行 if __name__ == '__main__':  冲突是pycharm和unittest调用方式不同

