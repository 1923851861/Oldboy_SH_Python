'''
1、守护进程
    守护进程其实就是一个“子进程”
    守护=》伴随
    守护进程会伴随主进程的代码运行完毕后而死掉

2、为何用守护进程
    关键字就两个：
        进程：
            当父进程需要将一个任务并发出去执行，需要将该任务放到一个子进程里
        守护：
            当该子进程内的代码在父进程代码运行完毕后就没有存在的意义了，就应该
            将该子进程设置为守护进程，会在父进程代码结束后死掉
'''

# from multiprocessing import Process
# import time,os
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=('守护进程',))
#     p2=Process(target=task,args=('正常的子进程',))
#
#     p1.daemon = True # 一定要放到p.start()之前
#     p1.start()
#     p2.start()
#
#     print('主')



#主进程代码运行完毕,守护进程就会结束
from multiprocessing import Process
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")

    '''
    main-------
    456
    enn456
    '''


    '''
    main-------
    123
    456
    enn456
    '''

    '''
    123
    main-------
    456
    end456
    '''
