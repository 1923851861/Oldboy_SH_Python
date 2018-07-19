'''
1、什么是GIL（这是Cpython解释器）
    GIL本质就是一把互斥锁，那既然是互斥锁，原理都一样，都是让多个并发线程同一时间只能
    有一个执行
    即：有了GIL的存在，同一进程内的多个线程同一时刻只能有一个在运行，意味着在Cpython中
        一个进程下的多个线程无法实现并行===》意味着无法利用多核优势
        但不影响并发的实现

    GIL可以被比喻成执行权限，同一进程下的所以线程 要想执行都需要先抢执行权限

2、为何要有GIL
    因为Cpython解释器自带垃圾回收机制不是线程安全的

3、如何用

    GIL vs 自定义互斥锁


        GIL相当于执行权限,会在任务无法执行的情况，被强行释放
        自定义互斥锁即便是无法执行，也不会自动释放


'''
from threading import Thread,Lock
import time

mutex=Lock()
n=100

def task():
    global n
    mutex.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    mutex.release()

if __name__ == '__main__':
    t_l=[]
    start_time=time.time()
    for i in range(3):
        t=Thread(target=task)
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

    stop_time=time.time()
    print(n)
    print(stop_time-start_time)