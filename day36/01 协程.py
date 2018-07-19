'''
1、协程：
    单线程实现并发
    在应用程序里控制多个任务的切换+保存状态
    优点：
        应用程序级别速度要远远高于操作系统的切换
    缺点：
        多个任务一旦有一个阻塞没有切，整个线程都阻塞在原地
        该线程内的其他的任务都不能执行了

        一旦引入协程，就需要检测单线程下所有的IO行为,
        实现遇到IO就切换,少一个都不行，以为一旦一个任务阻塞了，整个线程就阻塞了，
        其他的任务即便是可以计算，但是也无法运行了

2、协程序的目的：
    想要在单线程下实现并发
    并发指的是多个任务看起来是同时运行的
    并发=切换+保存状态
'''

#串行执行
# import time
#
# def func1():
#     for i in range(10000000):
#         i+1
#
# def func2():
#     for i in range(10000000):
#         i+1
#
# start = time.time()
# func1()
# func2()
# stop = time.time()
# print(stop - start)


#基于yield并发执行
# import time
# def func1():
#     while True:
#         print('func1')
#         yield
#
# def func2():
#     g=func1()
#     for i in range(10000000):
#         print('func2')
#         i+1
#         time.sleep(3)
#         next(g)
#
# start=time.time()
# func2()
# stop=time.time()
# print(stop-start)



# pip3 install gevent
# from gevent import monkey,spawn;monkey.patch_all()
# import time
#
# def eat(name):
#     print('%s eat 1' %name)
#     time.sleep(3)
#     print('%s eat 2' %name)
#
# def play(name):
#     print('%s play 1' %name)
#     time.sleep(1)
#     print('%s play 2' %name)
#
# start=time.time()
# g1=spawn(eat,'egon')
# g2=spawn(play,'zmy')
#
# g1.join()
# g2.join()
# print(time.time() - start)
# print(g1)
# print(g2)



from gevent import monkey,spawn;monkey.patch_all()
from threading import current_thread
import time

def eat():
    print('%s eat 1' %current_thread().name)
    time.sleep(3)
    print('%s eat 2' %current_thread().name)

def play():
    print('%s play 1' %current_thread().name)
    time.sleep(1)
    print('%s play 2' %current_thread().name)

g1=spawn(eat,)
g2=spawn(play,)

print(current_thread().name)
g1.join()
g2.join()

