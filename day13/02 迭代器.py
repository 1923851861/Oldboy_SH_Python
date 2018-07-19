'''
1、什么是迭代器
    迭代器即迭代取值的工具
    迭代：
        迭代是一个重复的过程，每一次重复都是基于上一次的结果而来的

        单纯的重复并不是迭代
        while True:
            print('1111')

        迭代：
        l=['a','b','c']

        def iterator(item):
            i=0
            while i < len(item):
                print(l[i])
                i+=1
        iterator(l)


2、 为什么要有迭代器
    基于索引的迭代器取值方式只适用于列表、元组、字符串类型
    而对于没有索引的字典、集合、文件，则不在适用
    所以必须找到一种通用的并且不依赖于索引的迭代器取值方式=》迭代器

    迭代器适用于可迭代的类型

3、如何用迭代器


'''


# l=['a','b','c']
# i=0
# while i < len(l):
#     print(l[i])
#     i+=1

# l = ['a', 'b', 'c']
# s='hello'
#
# def iterator(item): #item='hello'
#     i = 0
#     while i < len(item):
#         print(item[i])
#         i += 1
# # iterator(l)
# iterator(s)


# 可迭代的对象：在python中但凡内置有__iter__方法的对象都是可迭代的对象
# 字符串、列表、元组、字典、集合、文件都是可迭代的对象
# num1=10
# num2=10.1
# s1='hello'
# l=[1,2,3]
# t=(1,2,3)
# d={'x':1}
# s2={1,2,3}
# f=open('a.txt','w')
#
# s1.__iter__
# l.__iter__
# t.__iter__
# d.__iter__
# s2.__iter__
# f.__iter__


#
#
# 迭代器对象:指的是既内置有__iter__方法，又内置有__next__方法的对象
#执行可迭代对象的__iter__方法得到的就是内置的迭代器对象
# 文件对象本身就是迭代器对象

#强调：
#1、迭代器对象一定是可迭代的对象，反之则不然



# info={'name':'egon','age':18,'is_beautiful':True,'sex':'male'}
# info_iter=info.__iter__()
# # print(info_iter)
#
# res1=info_iter.__next__()
# print(res1)
#
# res2=info_iter.__next__()
# print(res2)
#
# res3=info_iter.__next__()
# print(res3)
#
# res4=info_iter.__next__()
# print(res4)
#
# info_iter.__next__() # 一旦迭代器取值取干净，再继续取就会抛出StopIteration



# info={'name':'egon','age':18,'is_beautiful':True,'sex':'male'}
# # info=[1,2,3,4,5]
# info_iter=info.__iter__()
# while True:
#     try:
#         print(info_iter.__next__())
#     except StopIteration:
#         break


#for循环：迭代器循环
# info={'name':'egon','age':18,'is_beautiful':True,'sex':'male'}
#in后跟的一定要是可迭代的对象
# for k in info: # info_iter=info.__iter__()
#     print(k)

# f=open('a.txt','r')
# for k in f:
#     print(k)


# 迭代器对象:指的是既内置有__iter__方法，又内置有__next__方法的对象
# 执行迭代器对象的__next__得到的是迭代器的下一个值
# 执行迭代器对象的__iter__得到的仍然是迭代器本身

# iter_info=info.__iter__()
# # print(iter_info)
# print(iter_info is iter_info.__iter__() is iter_info.__iter__().__iter__().__iter__().__iter__().__iter__())
#


#总结迭代器对象的优缺点：
#优点：
#1、提供了一种通用的、可以不依赖索引的迭代取值方式
#2、迭代器对象更加节省内存
# f=open('movie.tar.gz','rb')
# f.__ next__()
# f=open('db.txt','rt',encoding='utf-8')
#
# print(f.__next__())
# print(f.__next__())
# print(next(f)) #f.__next__()

# s='hello'
# print(s.__len__())
# print(len(s))
# s.__iter__()
# print(iter(s))


# 缺点：
#1、迭代器的取值不如按照索引的方式更灵活，因为它只能往后取不能往前退
#2、无法预测迭代器值的个数
# names=['egon','alex_SB','wxx_SB']
# iter_names=iter(names)
# print(next(iter_names))
# print(next(iter_names))
#
# iter_names=iter(names)
# print(next(iter_names))
# print(next(iter_names))
# # print(next(iter_names))
#
# print(names[1])
# print(names[1])



# s=set('helllllo')
# print(s)


# for i in 10:
#     pass

# list(10)

# names=['a','b','c','d']
# iter_names=iter(names)
#
# l1=list(iter_names)
# print(l1)
#
# l2=list(iter_names)
# print(l2)

# f=open('db.txt','rt',encoding='utf-8')
#
# print(list(f))
# print(list(f))
# print(list(f))
# print(list(f))
# print(list(f))


# l1=[1,2,3,]
# diedaiqi=l1.__iter__()
# print(list(l1))
# print(list(l1))
# print(list(l1))
# print(list(l1))
# print(list(l1))
# print(list(l1))


# name=['a','b','r','y','h']
# s=name[]
# print(s)


l=['a','b','c']

def iterator(item):
    i=0
    while i < len(item):
        print(l[i])
        i+=1
iterator(l)