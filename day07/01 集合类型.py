# pythoners=['王大炮','李二丫','陈独秀','艾里克斯','wxx','欧德博爱']
# linuxers=['陈独秀','wxx','egon','张全蛋']
#
# l1=[]
# for stu in pythoners:
#     if stu in linuxers:
#         # print(stu)
#         l1.append(stu)
#
# print(l1)
#
# l2=[]
# for stu in pythoners:
#     if stu not in linuxers:
#         # print(stu)
#         l2.append(stu)
#
# print(l2)



#一：基本使用
# 1 用途: 关系运算、去重
#
# 2 定义方式:{}内用逗号分隔开多个元素，每一个元素都必须是不可变（即可hash）类型
#强调：
#2.1 集合内元素都必须是不可变（即可hash）类型
#2.2 集合内的元素无序
#2.3 集合内的元素不能重复

# s={1,2,'a'} #s=set({1,2,'a'})
# print(type(s))

# s={1.1,1,'aa',(1,2,3),{'a':1}}

# s={1,'a','hello',(1,2,3),4}
# for item in s:
#     print(item)

# s={1,1,1,1,1,1,1,1,1,'a','b','a'}
# s={(1,2,3),(1,2,3),'a','b','a'}
# print(s)

# s=set('hello')
# print(s)

# 单纯的用集合去重，需要注意的问题是
#1、去重的目标所包含的值必须都为不可变类型
#2、去重的结果会打乱原来的顺序
# names=['asb','asb','asb','wsb','wsb','egon_nb']
# s=set(names)
# names=list(s)
# print(names)

#
# 3 常用操作+内置的方法
#优先掌握的操作：
#1、长度len
# pythoners={'王大炮','李二丫','陈独秀','艾里克斯','wxx','欧德博爱'}
# print(len(pythoners))

#2、成员运算in和not in
# print('李二丫' in pythoners)


# pythoners={'王大炮','李二丫','陈独秀','艾里克斯','wxx','欧德博爱'}
# linuxers={'陈独秀','wxx','egon','张全蛋'}
# # 3、|并集
# # print(pythoners | linuxers)
# print(pythoners.union(linuxers))

#4、&交集
# print(pythoners & linuxers)
# print(pythoners.intersection(linuxers))
# print(linuxers & pythoners)
#5、-差集
# print(pythoners - linuxers)
# print(pythoners.difference(linuxers))
# print(linuxers - pythoners)
# print(linuxers.difference(pythoners))
#6、^对称差集
# print(pythoners ^ linuxers)
# print(pythoners.symmetric_difference(linuxers))
#
# print(linuxers ^ pythoners)
#7、==
# s1={1,2,3}
# s2={1,2,3}
# print(s1 == s2)

#8、父集(包含关系)：>,>=
# s1={1,2,3,4,5}
# s2={1,2,3}
# print(s1 > s2) # s1包含s2
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

# s3={1,2,10}
# print(s1 > s3)

# s1={1,2,3,4,5}
# s2={1,2,3,4,5}
# print(s1 >= s2)

#9、子集(被包含的关系)：<,<=

# s1={1,2,3,4,5}
# s1.add(6)
# print(s1)

# s1.update({4,7,8,9})
# print(s1)


# res=s1.pop()
# print(res)

# s1={1,2,3,4,5,}
# res=s1.remove(4)
# print(res)
# print(s1)

# s1={1,2,3,4,5}
# s2={2,3,7,8}
# s1=s1 - s2
# print(s1)
# s1.difference_update(s2) # s1=s1 - s2
# print(s1)

# s1={1,2,3,4,5}
# s1.pop()
# s1.remove(7)
# s1.discard(7) # 即便要删除的元素不存在也不会报错

# s1={1,2,3,4,5}
# s2={5,6,7,8}
# print(s1.isdisjoint(s2))



#
# #二：该类型总结
# 1 存一个值or存多个值
#     可以存多个值，值都必须为不可变类型
#
# 2 有序or无序
# 无序
#
# 3 可变or不可变
# set集合是可变类型
# s={1,2,3}
# print(id(s))
# s.add(4)
# print(s)
# print(id(s))



#==============集合的去重===========
# 单纯的用集合去重，需要注意的问题是
#1、去重的目标所包含的值必须都为不可变类型
#2、去重的结果会打乱原来的顺序
# names=['asb','asb','asb','wsb','wsb','egon_nb',[1,2,3]]
# s=set(names)

# names=list(s)
# print(names)

# stu_info=[
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'alex','age':73,'sex':'male'},
#     {'name':'oldboy','age':84,'sex':'female'},
# ]
#
# new_info=[]
# for info in stu_info:
#     if info not in new_info:
#         new_info.append(info)
#
# print(new_info)


