# 信号量是控制同一时刻并发执行的任务数
from threading import Thread,Semaphore,current_thread
import time,random

sm=Semaphore(5)

def task():
    with sm:
        print('%s 正在上厕所' %current_thread().name)
        time.sleep(random.randint(1,4))


if __name__ == '__main__':
    for i in range(20):
        t=Thread(target=task)
        t.start()