# print('run......................')

xxx=111
yyy=222

# def f1():
#     print('111111111111')
#
# def f2():
#     print('22222222222222222')

# import m1
# import m2
# from aaa import m1
# from aaa import m2

# 在当前位置拿到f1与f2
# 绝对导入
# from aaa.m1 import f1
# from aaa.m2 import f2

# 相对导入
# .代表当前被导入文件所在的文件夹
# ..代表当前被导入文件所在的文件夹的上一级
# ...代表当前被导入文件所在的文件夹的上一级的上一级
from .m1 import f1
from .m2 import f2


# bbb=3333
# from aaa import bbb
from . import bbb