# author:ToddCombs
# 导入整个模块
# 给形参指定默认值或函数调用关键字实参时，等号两边不要有空格
import pizza
# 导入模块时可以给模块指定别名，但该模块中所有函数名称都没变。
import pizza as p
# 使用*让python导入模块中所有函数，但不建议调用非自己写的大型模块，如果导入模块中有函数名与自己项目使用相同的名称则会导致逻辑混乱。
from pizza import *
# 导入部分函数,若使用导入部分函数的语法，则调用函数时无需使用句点。
from pizza import make_pizza_one
# 使用as给函数指定别名，如果导入函数名与程序中现有名称冲突，可指定简短独一无二的别名。
from pizza import make_pizza_one as mp

pizza.make_pizza_one(17, 'pepperoni')
pizza.make_pizza_one(13, 'mushrooms', 'green peppers', 'extra cheese')

# 调用函数时使用重新明明的p.来调用
p.make_pizza_one(20,'pepperoni')

make_pizza_one(18, 'pepperoni')
make_pizza_one(14, 'mushrooms', 'green peppers', 'extra cheese')

mp(19, 'pepperoni')
mp(15, 'mushrooms', 'green peppers', 'extra cheese')

# 由于使用*号导入了所有函数，调用时可以使用名称调用每个函数无需使用句点方式调用。
make_pizza_one(21,'pepperoni')