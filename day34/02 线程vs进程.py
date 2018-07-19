#1、线程的开启速度快
# from threading import Thread
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=task,args=('子线程',))
#     # t=Process(target=task,args=('子进程',))
#     t.start()
#     print('主')


#2、同一进程下的多个线程共享该进程内的数据
# from threading import Thread
# import time
#
# x=100
# def task():
#     global x
#     x=0
#
# if __name__ == '__main__':
#     t=Thread(target=task,)
#     t.start()
#     # time.sleep(3)
#     t.join()
#     print('主',x)


# 查看pid
from threading import Thread
import time,os

def task():
    print(os.getpid())

if __name__ == '__main__':
    t=Thread(target=task,)
    t.start()
    print('主',os.getpid())
