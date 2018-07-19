'''

1 什么是生成器？
在函数内但凡出现yield关键字，再调用函数就不会执行函数体代码，会返回值一个值，该值称之为生成器
 生成器本质就是迭代器

2、为什么要有生成器？
    生成器是一种自定义迭代器的方式

3、如何用生成器


'''



# def func():
#     print('first1')
#     print('first2')
#     print('first3')
#     yield 1 #暂停
#     print('second1')
#     print('second2')
#     print('second3')
#     yield 2  #暂停
#     print('third')
#     yield 3 #暂停
#     print('fourth')
#
# g=func()
# print(g)
# print(g.__iter__().__iter__().__iter__() is g)
# res1=next(g)
# print('第一次的返回值：',res1)
#
# print('='*100)
# res2=next(g)
# print('第二次的返回值：',res2)
#
# print('='*100)
# res3=next(g)
# print('第三次的返回值：',res3)
#
# print('='*100)
# res4=next(g)
# print('第三次的返回值：',res4)

# for item in g: #g=iter(g) #item=next(g)
#     print(item)

# i=range(1,1000)
# for item in range(1,100000000000000):
#     print(item)


#
# def my_range(start,stop,step=1):
#     while start < stop:
#         yield start # 暂停
#         start+=step
# g=my_range(1,5,2) #1 3
#
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# for item in g:
#     print(item)


#总结yield的功能
#1、提供一种自定义迭代器的方式
#2、yield可以暂停住函数，返回值

#yield  VS return
#相同点：都是用在函数内，都可以返回值，没有类型限制，没有个数限制
#不同点：return只能返回一次值，yield可以返回多次值


# 了解知识
# yield 值
# x=yield
# x= yield 值

# def dog(name):
#     food_list=[]
#     print('狗哥 %s 准备开吃' %name)
#     while True:
#         food=yield food_list#暂停 food=yield='一桶泔水'
#         print('狗哥[%s]吃了<%s>' %(name,food))
#         food_list.append(food)
#
#
# alex_dog=dog('alex')
#
# res1=next(alex_dog) # 初始化，即让狗准备好
# print(res1)
# next(alex_dog) # 等同于alex_dog.send(None)
# #
# next(alex_dog)
#
# res2=alex_dog.send(('一泡翔','咖啡伴侣'))
# print(res2)
# #
# res3=alex_dog.send('一桶泔水')
# print(res3)


















