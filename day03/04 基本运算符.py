
# print(1 + 2)
# x=10
# y=20
# res=x + y
# print(res)

# /是有零有整
# print(10 / 3)
#// 地板除，只取整数部分

# print(10 // 3)
# print(10 // 4)


# % ：取余数
# print(10 % 3)

# print(10 ** 2)


# pwd='123'
# print(pwd != '123')


# 列表之间比较大小，仅限于相同位置对应的值是同一类型
# l1=[1,'a',3]
# l2=[1,3]
#
# print(l2 > l1)

# print(10 > 1.1)


#
# age=18
#
# # age+=1 #age=age + 1
# # age*=10 #age=age*10
# age//=3 #age=age//3
# print(age)
#

# 重点：
# 链式赋值
# d=10
# c=d
# b=d
# a=d
#
# a=b=c=d=10
# print(a,b,c,d)

# 交叉赋值
# x=100
# y=200

# temp=x
# x=y
# y=temp
# print(x,y)

# x,y=y,x
# print(x,y)


# 变量值的解压缩
# l=['egon','asb','wsb']
# x=l[0]
# y=l[1]
# z=l[2]
# # x,y,z=l
#
# print(x,y,z)

# l=['egon','asb','wsb','lsb']
# x,y,z,a=l
# print(x,y,z,a)
# _='lsb'
# x,_,z,_=l
#
# print(_)

# yj=[11,22,33,44,55,66,77,88,99,100,200,300]
# mon1,mon2,mon3,mon4,mon5,mon6,*_=yj
# # print(mon1)
# # print(mon2)
# # print(mon3)
# # print(mon4)
# # print(mon5)
# # print(mon6)
# print(*_)
# mon1,mon2,*_,mon11,mon12=yj
#
# print(mon1)
# print(mon2)
# print(mon11)
# print(mon12)


# 对于字典来收，解压出来的是key
# info={'name':'egon','age':18,'sex':'male'}
#
# x,y,z=info
# print(x,y,z)




#逻辑运算
# print(not 10 > 3)

# print(10 > 3 and 3 > 2)
#
# print(3 >= 3 and 3 > 2 and 'xxx' != 'egon' and 3 > 2)


# print(False or True)
# print(3 > 3 or 3 > 2 or 'xxx' != 'egon' or 3 > 2)

# print(not 3 > 3 or (not 3 > 2 and 'xxx' == 'egon' or 3 > 2))



#
# if 3 >= 3 and 3 > 2:
#     if 'xxx' != 'egon' and 3 > 2:
#         print('===>')

# print(3 >= 3 and 3 > 2 and 'xxx' != 'egon' and 3 > 2)


# 练习：
# x=100
# y=200
#
# x,y=y,x
#
# print(x)
# print(y)


