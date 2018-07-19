from multiprocessing import Process
import time
import os

def task():
    print('%s is running' %os.getpid())
    time.sleep(3)
    print('%s is done' % os.getpid())

if __name__ == "__main__":
    p=Process(target=task)
    p.start() # 仅仅只是向操作系统发送一个开启进程的信号
    print(p.pid)

    p.join() # 等到子进程p执行完毕后，将p占用的操作系统的pid回收
    print(p.pid)
    # print(x)

    print('主')