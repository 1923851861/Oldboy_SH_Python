# # # 方式一：
from multiprocessing import Process
import time

def task(x):
    print('%s is running' %x)
    time.sleep(3)
    print('%s is done' %x)

if __name__ == '__main__':
    # Process(target=task,kwargs={'x':'子进程'})
    p=Process(target=task,args=('子进程',)) # 如果args=(),括号内只有一个参数，一定记住加逗号
    p.start() # 只是在操作系统发送一个开启子进程的信号

    print('主')




# 方式二：
from multiprocessing import Process
import time

class Myprocess(Process):
    def __init__(self,x):
        super().__init__()
        self.name=x

    def run(self):
        print('%s is running' %self.name)
        time.sleep(3)
        print('%s is done' %self.name)

if __name__ == '__main__':
    p=Myprocess('子进程1')
    p.start()  #p.run()
    print('主')



# from multiprocessing import Process
# import time


# def task(x,n):
#     print('%s is running' % x)
#     time.sleep(n)
#     print('%s is done' % x)
#
#
# if __name__ == '__main__':
#     # Process(target=task,kwargs={'x':'子进程'})
#     p1 = Process(target=task, args=('子进程1',3))  # 如果args=(),括号内只有一个参数，一定记住加逗号
#     p2 = Process(target=task, args=('子进程2',5))  # 如果args=(),括号内只有一个参数，一定记住加逗号
#     p1.start()  # 只是在操作系统发送一个开启子进程的信号
#     p2.start()  # 只是在操作系统发送一个开启子进程的信号
#
#     print('主')

