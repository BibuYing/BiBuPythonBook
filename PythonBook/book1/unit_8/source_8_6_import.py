# 使用模块

#导入特定模块
from book1.unit_8 import pizza
pizza.make_pizza(16, 'pepperoni')

#导入特定函数
from book1.unit_8.pizza import make_pizza
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#为导入的模块指定名字
from book1.unit_8 import pizza as p
p.make_pizza(16, 'pepperoni')

#导入模块里面所有函数(不建议使用，直接导入整个模块，使用句点表示法)
from book1.unit_8.pizza import *
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')