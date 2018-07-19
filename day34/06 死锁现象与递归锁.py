from threading import Thread,Lock,active_count,RLock
import time

mutexA=Lock()
mutexB=Lock()
# obj=RLock() #递归锁的特点：可以连续的acquire
# mutexA=obj
# mutexB=obj

class Mythread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到A锁' %self.name)

        mutexB.acquire()
        print('%s 拿到B锁' %self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到B锁' %self.name)
        time.sleep(1)

        mutexA.acquire()
        print('%s 拿到A锁' %self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t=Mythread()
        t.start()
    print(active_count())