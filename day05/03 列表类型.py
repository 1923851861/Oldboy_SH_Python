#作用：多个装备，多个爱好，多门课程，多个女朋友等

#定义：[]内可以有多个任意类型的值，逗号分隔
# my_girl_friends=['alex','wupeiqi','yuanhao',4,5] #本质my_girl_friends=list([...])
#
# l=list('hello') # list内只能跟能够被for循环遍历的数据类型
# print(l)
# l=list({'a':1,'b':2})
# print(l)

#优先掌握的操作：
#1、按索引存取值(正向存取+反向存取)：即可存也可以取
# names=['alex','wxx','lxx','egon']
# names[0]='ALEX'

# print(names)
#2、切片(顾头不顾尾，步长)
# names=['alex','wxx','lxx','egon']
# print(names[0:3])

#3、长度
# names=['alex','wxx','lxx','egon']
# print(len(names))

#4、成员运算in和not in
# names=['alex','wxx','lxx','egon',4]
# print(4 in names)


#5、追加
# names=['alex','wxx','lxx','egon']
# names.append('cxx1')
# names.append('cxx2')
# names.append('cxx3')
# print(names)

#6、删除
# names=['alex','wxx','lxx','egon']
# del names[2]

# print(names)

#7、循环
# names=['alex','wxx','lxx','egon']
# for name in names:
#     print(name)

# 需要掌握的操作(****)
# names=['alex','wxx','lxx','egon',4,3.1]
# names.insert(1,'SB')
# print(names)

# names=['alex','wxx','lxx','egon',4,3.1]
# res=names.remove('wxx')  # 单纯的删掉,是按照元素的值去删除，没有返回值
# print(res)
# print(names)


# names=['alex','wxx','lxx','egon',4,3.1]
# res=names.pop(1) #拿走一个值,是按照索引去删除,有返回值
# print(names)
# print(res)

# names=['alex','wxx','lxx','egon',4,3.1]
# print(names.pop())
# print(names.pop())

# names=['alex','wxx','lxx','lxx','egon',4,3.1]
# print(names.count('lxx'))

# print(names.index('lxx'))

# names.clear()
# print(names)

# x=names.copy()
# print(x)

# name=names.extend([1,2,3])
# print(name)
#
# names.reverse()
# print(names)

# names=[1,10,-3,11]
# names.sort(reverse=True)
# print(names)


#二：该类型总结
# 1 存一个值or存多个值
#     可以存多个值，值都可以是任意数据类型
#
# 2 有序or无序
# 有序
# 3 可变or不可变
# 可变

# l=['a','b']
# print(id(l))
# l[0]='A'
# print(id(l))