# 守护线程会在本进程内所有非守护的线程都死掉了才跟着死
# 即：
# 守护线程其实守护的是整个进程的运行周期（进程内所有的非守护线程都运行完毕）
from threading import Thread,current_thread
import time


def task():
    print('%s is running' % current_thread().name)
    time.sleep(3)
    print('%s is done' % current_thread().name)


if __name__ == '__main__':
    t = Thread(target=task,name='守护线程')
    t.daemon=True
    t.start()
    print('主')

#
# from threading import Thread
# import time
#
# def foo():
#     print(123)
#     time.sleep(3)
#     print("end123")
#
# def bar():
#     print(456)
#     time.sleep(1)
#     print("end456")
#
#
# t1=Thread(target=foo)
# t2=Thread(target=bar)
#
# t1.daemon=True
# t1.start()
# t2.start()
# print("main-------")
#
# '''
# 123
# 456
# main-------
# end456
#
# '''

