'''
1、什么是装饰器
    器指的是工具，而程序中的函数就具备某一功能的工具
    装饰指的是为被装饰器对象添加额外功能

    就目前的知识来看：
        定义装饰器就是定义一个函数，只不过该函数的功能是用来为
        其他函数添加额外的功能

    其实：
        装饰器本身其实可以是任意可调用的对象
        被装饰的对象也可以是任意可调用的对象


2、为什么要用装饰器
    软件的维护应该遵循开放封闭原则
    开放封闭原则指的是：
        软件一旦上线运行后对修改源代码是封闭的，对扩展功能的是开放的
        这就用到了装饰器

    装饰器的实现必须遵循两大原则：
        1、不修改被装饰对象的源代码
        2、不修改被装饰对象的调用方式
    装饰器其实就在遵循1和2原则的前提下为被装饰对象添加新功能

3、如何用装饰器
'''

# import time
#
# def index():
#     start=time.time()
#     print('welcome to index')
#     time.sleep(3)
#     stop=time.time()
#     print('run time is %s' %(stop-start))
# index()

#######
# import time
#
# def index():
#     print('welcome to index')
#     time.sleep(3)
#
# def f2():
#     print('from f2')
#     time.sleep(2)
#
# start=time.time()
# index()
# stop=time.time()
# print('run time is %s' %(stop-start))
#
# start=time.time()
# f2()
# stop=time.time()
# print('run time is %s' %(stop-start))





# import time
#
# def index():
#     print('welcom to index')
#     time.sleep(3)
#
# def timmer(func):
#     start=time.time()
#     func()
#     stop=time.time()
#     print('run time is %s' %(stop-start))
#
# timmer(index)




'''
import time

def index():
    print('welcome to index')
    time.sleep(3)

def timmer(func): #func=最原始的index
    # func=index
    def inner():
        start=time.time()
        func()
        stop=time.time()
        print('run time is %s' %(stop-start))
    return inner

# f=timmer(index)
# f()

# index=timmer(被装饰函数的内存地址)
index=timmer(index) #index=inner

index() #inner()


'''
# import time
#
# def index():
#     print('welcome to index')
#     time.sleep(3)
#
# def timmer(func):
#     #func=最原始的index
#     def wrapper():
#         start=time.time()
#         func()
#         stop=time.time()
#         print('run time is %s' %(stop - start))
#     return wrapper
#
# index=timmer(index) #index=wrapper函数的内存地址
# index()
#
#
#抄写五遍
# import time
# def index():
#     print('welcome to index')
#     time.sleep(3)
# def timmer(func):
#     #func=最原始的index
#     def wrapper():
#         start=time.time()
#         func()
#         stop=time.time()
#         print('run time is %s' %(stop-start))
#     return wrapper
#
# index=timmer(index) #index=wrapper函数的内存地址
#
# index()

# import time
#
# def index():
#     print('welcome to index')
#     time.sleep(2)
#
# def timmer(func):
#     def wrapper():
#         start=time.time()
#         func()
#         stop=time.time()
#         print('run time is %s' %(stop-start))
#     return wrapper
#
# index=timmer(index)
# index()

# import time
#
# def index():
#     print('welcome to index')
#     time.sleep(3)
# def timmer(func):
#     def wrapper():
#         start=time.time()
#         func()
#         stop=time.time()
#         print('run time is %s' %(stop-start))
#     return wrapper
# index=timmer(index)
# index()

# import time
#
# def index():
#     print('welcome to index')
#     time.sleep(3)
# def timmer(func):
#     def wrapper():
#         start=time.time()
#         func()
#         stop=time.time()
#         print('run time is %s' %(stop-start))
#     return wrapper
# index=timmer(index)
# index()

import time

def index():
    print('welcome to index')
    time.sleep(3)
def timmer(func):
    def wrapper():
        start=time.time()
        func()
        stop=time.time()
        print('run time is %s' %(stop-start))
    return wrapper
index=timmer(index)
index()
