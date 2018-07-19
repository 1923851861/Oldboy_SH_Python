'''
1 什么是生产者消费者模型
    生产者:比喻的是程序中负责产生数据的任务
    消费者:比喻的是程序中负责处理数据的任务

    生产者->共享的介质(队列)<-消费者

2 为何用
    实现了生产者与消费者的解耦和,生产者可以不停地生产,消费者也可以不停地消费
    从而平衡了生产者的生产能力与消费者消费能力,提升了程序整体运行的效率

    什么时候用?
        当我们的程序中存在明显的两类任务,一类负责产生数据,另外一类负责处理数据
        此时就应该考虑使用生产者消费者模型来提升程序的效率


'''
# from multiprocessing import Queue, Process
# import time
# import os
# import random
#
#
# def producer(q):
#     for i in range(10):
#         res = '包子%s' % i
#         time.sleep(random.randint(1, 3))
#         # 往队列里丢
#         q.put(res)
#         print('\033[45m%s 生产了 %s\033[0m' % (os.getpid(), res))
#     q.put(None)
#
#
# def consumer(q):
#     while True:
#         # 从队列里取走
#         res = q.get()
#         if res is None: break
#         time.sleep(random.randint(1, 3))
#         print('\033[46m%s 吃了 %s\033[0m' % (os.getpid(), res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者们
#     p1 = Process(target=producer, args=(q,))
#     # 消费者们
#     c1 = Process(target=consumer, args=(q,))
#
#     p1.start()
#     c1.start()
#
#     print('主')


#
# from multiprocessing import Queue,Process
# import time
# import os
# import random
#
# def producer(name,food,q):
#     for i in range(3):
#         res='%s%s' %(food,i)
#         time.sleep(random.randint(1,3))
#         # 往队列里丢
#         q.put(res)
#         print('\033[45m%s 生产了 %s\033[0m' %(name,res))
#     # q.put(None)
#
# def consumer(name,q):
#     while True:
#         #从队列里取走
#         res=q.get()
#         if res is None:break
#         time.sleep(random.randint(1,3))
#         print('\033[46m%s 吃了 %s\033[0m' %(name,res))
#
# if __name__ == '__main__':
#     q=Queue()
#     # 生产者们
#     p1=Process(target=producer,args=('egon','包子',q,))
#     p2=Process(target=producer,args=('杨军','泔水',q,))
#     p3=Process(target=producer,args=('猴老师','翔',q,))
#     # 消费者们
#     c1=Process(target=consumer,args=('Alex',q,))
#     c2=Process(target=consumer,args=('wupeiqidsb',q,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     # 在p1\p2\p3都结束后,才应该往队列里放结束信号,有几个消费者就应该放几个None
#     q.put(None)
#     q.put(None)
#
# # print('主')


from multiprocessing import JoinableQueue, Process
import time
import random


def producer(name, food, q):
    for i in range(3):
        res = '%s%s' % (food, i)
        time.sleep(random.randint(1, 3))
        # 往队列里丢
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' % (name, res))
    # q.put(None)


def consumer(name, q):
    while True:
        # 从队列里取走
        res = q.get()
        if res is None: break
        time.sleep(random.randint(1, 3))
        print('\033[46m%s 吃了 %s\033[0m' % (name, res))
        q.task_done()   #消费者的一次任务已经结束


if __name__ == '__main__':
    q = JoinableQueue()  # 这就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。
    # 生产者们
    p1 = Process(target=producer, args=('egon', '包子', q,))
    p2 = Process(target=producer, args=('杨军', '泔水', q,))
    p3 = Process(target=producer, args=('猴老师', '翔', q,))
    # 消费者们
    c1 = Process(target=consumer, args=('Alex', q,))
    c2 = Process(target=consumer, args=('wupeiqidsb', q,))
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

    q.join()  # 等待队列被取干净
    # q.join() 结束意味着
    # 主进程的代码运行完毕--->(生产者运行完毕)+队列中的数据也被取干净了->消费者没有存在的意义

    # print('主')
