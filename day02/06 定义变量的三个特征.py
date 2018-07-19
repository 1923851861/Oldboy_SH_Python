# x='egon'
#
# #id
# print(id(x))
# #类型
# print(type(x))
# #值
# print(x)

#判断值是否相等：==
# name1='egon'
# name2='egon'
# print(name1 == name2)

#判断id是否相等:is
x=11
y=x
# print(x == y)
print(x is y)


#总结：
#1、id相等，值一定相等
#2、值相等，id却不一定一样


'''
>>> x='info<egon:18>'
>>> y='info<egon:18>'
>>>
>>>
>>>
>>> id(x)
1484352906224
>>> id(y)
1484352906416
>>>
>>> x is y
False
>>> x == y
True
'''