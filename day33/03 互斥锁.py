#互斥锁：可以将要执行任务的部分代码（只涉及到修改共享数据的代码）变成串行
#join：是要执行任务的所有代码整体串行
from multiprocessing import Process,Lock
import json
import os
import time
import random

def check():
    time.sleep(1) # 模拟网路延迟
    with open('db.txt','rt',encoding='utf-8') as f:
        dic=json.load(f)
    print('%s 查看到剩余票数 [%s]' %(os.getpid(),dic['count']))

def get():
    with open('db.txt','rt',encoding='utf-8') as f:
        dic=json.load(f)
    time.sleep(2)
    if dic['count'] > 0:
        # 有票
        dic['count']-=1
        time.sleep(random.randint(1,3))
        with open('db.txt','wt',encoding='utf-8') as f:
            json.dump(dic,f)
        print('%s 购票成功' %os.getpid())
    else:
        print('%s 没有余票' %os.getpid())


def task(mutex):
    # 查票
    check()

    #购票
    mutex.acquire() # 互斥锁不能连续的acquire，必须是release以后才能重新acquire
    get()
    mutex.release()



    # with mutex:
    #     get()

if __name__ == '__main__':
    mutex=Lock()
    for i in  range(10):
        p=Process(target=task,args=(mutex,))
        p.start()
        # p.join()