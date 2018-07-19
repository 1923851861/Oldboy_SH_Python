'''
1、什么时候用池：
    池的功能是限制启动的进程数或线程数，
    什么时候应该限制？？？
    当并发的任务数远远超过了计算机的承受能力时，即无法一次性开启过多的进程数或线程数时
    就应该用池的概念将开启的进程数或线程数限制在计算机可承受的范围内

2、同步vs异步
    同步、异步指的是提交任务的两种方式

    同步：提交完任务后就在原地等待，直到任务运行完毕后拿到任务的返回值，再继续运行下一行代码
    异步：提交完任务（绑定一个回调函数）后根本就不在原地等待，直接运行下一行代码，等到任务有返回值后会自动触发回调函数




'''
#
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os
# import time
# import random
#
# def task(n):
#     print('%s run...' %os.getpid())
#     time.sleep(10)
#     return n**2
#
# def parse(res):
#     print('...')
#
# if __name__ == '__main__':
#     pool=ProcessPoolExecutor(4)
#     # pool.submit(task,1)
#     # pool.submit(task,2)
#     # pool.submit(task,3)
#     # pool.submit(task,4)
#
#     l=[]
#     start=time.time()
#     for i in range(1,5):
#         future=pool.submit(task,i)
#         l.append(future)
#         # print(future)
#         # print(future.result())
#
#     pool.shutdown(wait=True) #shutdown关闭进程池的入口
#     for future in l:
#         # print(future.result())
#         parse(future.result())
#     stop=time.time()
#     print('主',stop-start)






# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os
# import time
# import random
#
# def task(n):
#     print('%s run...' %os.getpid())
#     time.sleep(5)
#     return n**2
#
# def parse(future):
#     time.sleep(1)
#     res=future.result()
#     print('%s 处理了 %s' %(os.getpid(),res))
#
# if __name__ == '__main__':
#     pool=ProcessPoolExecutor(4)
#     # pool.submit(task,1)
#     # pool.submit(task,2)
#     # pool.submit(task,3)
#     # pool.submit(task,4)
#
#     start=time.time()
#     for i in range(1,5):
#         future=pool.submit(task,i)
#         future.add_done_callback(parse) # parse会在futrue有返回值时立刻触发，并且将future当作参数传给parse
#     pool.shutdown(wait=True) #shutdown关闭进程池的入口
#     stop=time.time()
#     print('主',os.getpid(),(stop - start))


from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import current_thread
import os
import time
import random

def task(n):
    print('%s run...' %current_thread().name)
    time.sleep(5)
    return n**2

def parse(future):
    time.sleep(1)
    res=future.result()
    print('%s 处理了 %s' %(current_thread().name,res))

if __name__ == '__main__':
    pool=ThreadPoolExecutor(4)
    start=time.time()
    for i in range(1,5):
        future=pool.submit(task,i)
        future.add_done_callback(parse) # parse会在futrue有返回值时立刻触发，并且将future当作参数传给parse
    pool.shutdown(wait=True) #shutdown关闭进程池的入口
    stop=time.time()
    print('主',current_thread().name,(stop - start))


