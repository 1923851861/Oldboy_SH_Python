# 主进程等子进程是因为主进程要给子进程收尸
# 进程必须等待其内部所有线程都运行完毕才结束
# from threading import Thread
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)
# if __name__ == '__main__':
#     t=Thread(target=task,args=('子线程',))
#     t.start()
#     print('主')
#


from threading import Thread,current_thread,active_count,enumerate
import time


def task():
    print('%s is running' % current_thread().name)
    time.sleep(3)
    print('%s is done' % current_thread().name)


if __name__ == '__main__':
    t = Thread(target=task,name='xxx')
    t.start()
    # t.join()
    # print(t.is_alive())
    # print(t.getName())
    # print(t.name)
    # print('主',active_count())
    # print(enumerate())

    # t.join()
    current_thread().setName('主线程')
    print('主',current_thread().name)
