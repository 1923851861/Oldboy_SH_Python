# import aaa
# 首次导入的模块发生三件事
#1、创建一个包的名称空间
#2、执行包下的__init__.py文件，将执行过程中产生的名字存放于包名称空间中
#    （即包名称空间中存放的名字都是来自于__init__.py）
#3、在当前执行文件中拿到一个名字aaa,aaa是指向包的名称空间的


# print(aaa.xxx)
# print(aaa.yyy)


# aaa.m1.f1()
# aaa.m2.f2()

# aaa.f1()
# aaa.f2()

# print(aaa.bbb)

# print(aaa.bbb.zzz)
# aaa.bbb.m3.f3()

# print(aaa.xxx)
# print(aaa.yyy)
# aaa.f1()
# aaa.f2()
# print(aaa.bbb)

# aaa.bbb.m3.f3()


import aaa
aaa.bbb.m3.f3()


