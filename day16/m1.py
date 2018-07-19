print('正在执行m1.py')

# def func1():
#     from m2 import x
#     print(x)

y='m1'
from m2 import x
# 1、创建m2的名称空间
#2、执行m2.py ，产生名字丢到m2的名称空间
#3、在当前文件中拿到x




'''
正在执行m1.py
正在执行m2.py
正在执行m1.py
'''