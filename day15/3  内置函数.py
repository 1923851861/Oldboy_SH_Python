
# 掌握
# res='你好'.encode('utf-8')
# print(res)
#
# res=bytes('你好',encoding='utf-8')
# print(res)

# 参考ASCII表将数字转成对应的字符
# print(chr(65))
# print(chr(90))
# 参考ASCII表将字符转成对应的数字
# print(ord('A'))

# print(divmod(10,3))


# l=['a','b','c']
# for item in enumerate(l):
#     print(item)

# l='[1,2,3]'
# l1=eval(l)
# print(l1,type(l1))
# print(l1[0])

# with open('a.txt',encoding='utf-8') as f:
#     data=f.read()
#     print(data,type(data))
#     dic=eval(data)
#     print(dic['sex'])

# print(pow(3,2,2)) # (3 ** 2) % 2

# print(round(3.3))

# print(sum(range(101)))


module=input('请输入你要导入的模块名>>: ').strip() #module='asdfsadf'
m=__import__(module)
print(m.time())



# 面向对象里的重点
classmethod
staticmethod
property

delattr
hasattr
getattr
setattr

isinstance
issubclass

object

super


# 了解
# print(abs(-13))
# print(all([1,2,3,]))
# print(all([]))

# print(any([0,None,'',1]))
# print(any([0,None,'',0]))
# print(any([]))

# print(bin(3)) #11
# print(oct(9)) #11
# print(hex(17)) #11

# print(callable(len))

# import time
# print(dir(time)) #列举出所有:time.名字


# s=frozenset({1,2,3}) # 不可变集合
# s1=set({1,2,3}) # 可变集合

# a=1111111111111111111111111111111111111111111111
# # print(globals())
# # print(locals())
# def func():
#     x=222222222
#     # print(globals())
#     print(locals())
# func()

# hash([1,2,3])

# def func():
#     """
#     文档注释
#     :return:
#     """
#     pass
#
# print(help(func))

# l=['a','b','c','d','e']
# s=slice(1,4,2)
# print(l[1:4:2])
# print(l[s])

# print(vars())