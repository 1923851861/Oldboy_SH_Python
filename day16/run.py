# 当前的执行文件
# x=1
# y=2
# 首次导入模块发生了3件事：
#1、以模块为准创造一个模块的名称空间
#2、执行模块对应的文件，将执行过程中产生的名字都丢到模块的名称空间
#3、在当前执行文件中拿到一个模块名
# import spam


# 之后的重复导入会直接引用之前创造好的结果，不会重复执行模块的文件
# import spam #spam=spam=模块名称空间的内存地址

# spam.名字
# print(x)
# spam.x
# print(spam.money)
# print(spam.read1)
# print(spam.read2)
# print(spam.change)
# money=11111111111111
# spam.read1()
# def read1():
#     print('执行文件的read1')
# spam.read2()

# spam.change()
# print(spam.money)
# print(money)

# import spam as sm
# print(sm.money)

# import time,spam,os,sys
# import spam
# import os
# import sys


# import spam
# spam.money

# from ... import ...首次导入也发生了三件事：
#1、以模块为准创造一个模块的名称空间
#2、执行模块对应的文件，将执行过程中产生的名字都丢到模块的名称空间
#3、在当前执行文件的名称空间中拿到一个名字，该名字直接指向模块中的某一个名字，意味着可以不用加任何前缀而直接使用

# x=1
# y=2
#
# from spam import money,read1
# money=10
# print(money)
# print(read1)

# from .... import ... 对比 import 。。。
# 优点：不用加前缀，代码更为精简
# 缺点：容易与当前执行文件中名称空间中的名字冲突

# 相同点：
# 1、都会执行模块对应的文件，都会产生模块的名称空间
# 2、调用功能时，需要跑到定义时寻找作用域关系，与调用位置无关
# 不同点
# 1、一种需要加前缀，一种不需要加前缀


# from spam import money,read1,read2,change
# money=111111111111111111
# read1()
# def read1():
#     print('当前执行文件的read1',money)

# read1()

# def read1():
#     print('当前执行文件的read1',money)

# read2()

# change=1
# change()
# print(money)


# from spam import money
# from spam import read1
# from spam import read2
# from spam import change

from spam import *
print(money)
print(read1)

print(change)
# print(read2)