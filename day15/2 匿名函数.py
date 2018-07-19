
# 有名函数：基于函数名重复使用
# def func():
#     print('from func')

# func()
# func()
# func()

# 匿名函数:没有绑定名字的下场是用一次就回收了
# def func(x,y): #func=函数的内存地址
#     return x + y

# res=(lambda x,y:x+y)(1,2)
# print(res)

# f=lambda x,y:x+y
# print(f)
# print(f(1,2))

# max min map filter sorted
# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }

# max的工作原理
#1 首先将可迭代对象变成迭代器对象
#2 res=next(可迭代器对象),将res当作参数传给key指定的函数,然后将该函数的返回值当作判断依据
# def func(k):
#     return salaries[k]
#
# print(max(salaries,key=func)) #next(iter_s)
# 'egon', v1=func('egon')
# 'alex', v2=func('alex')
# 'wupeiqi', v3=func('wupeiqi')
# 'yuanhao', v4=func('yuanhao')



# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# print(max(salaries,key=lambda k:salaries[k])) #next(iter_s)
# print(min(salaries,key=lambda k:salaries[k])) #next(iter_s)


# l=[10,1,3,-9,22]
# l1=sorted(l,reverse=False)
# print(l1)

# l=[1,4,3,9,6,5,-4,-6,-3]
# l1=sorted(l,reverse=True)
# print(l1)
# l2=sorted(l,reverse=True)
# print(l2)

# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# l=sorted(salaries,key=lambda k:salaries[k],reverse=True)
# print(l)


# print(sorted(salaries,key=lambda k:salaries[k],reverse=True))

# names=['张明言','刘华强','苍井空','alex']

# map的工作原理
#1 首先将可迭代对象变成迭代器对象
#2 res=next(可迭代器对象),将res当作参数传给第一个参数指定的函数,然后将该函数的返回值当作map的结果之一
# aaa=map(lambda x:x+"_SB",names)
# print(aaa)
# print(list(aaa))

# print([name+"_SB" for name in names])

# filter的工作原理
#1 首先将可迭代对象变成迭代器对象
#2 res=next(可迭代器对象),将res当作参数传给第一个参数指定的函数,然后filter会判断函数的返回值的真假,如果为真则留下res
# names=['alexSB','egon','wxxSB','OLDBOYSB']

# print([name for name in names if name.endswith('SB')])

# aaa=filter(lambda x:x.endswith('SB'),names)
# print(aaa)
# print(list(aaa))





