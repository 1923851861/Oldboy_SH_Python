#1、join
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running ' %name)
#     time.sleep(3)
#     print('%s is done ' % name)
#
#
# if __name__ == '__main__':
#     p=Process(target=task,args=('子进程1',))
#     p.start()
#     p.join() # 让父进程在原地等待，等到子进程运行完毕后，才执行下一行代码
#     print('主')



# from multiprocessing import Process
# import time
#
# def task(name,n):
#     print('%s is running ' %name)
#     time.sleep(n)
#     print('%s is done ' % name)
#
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=('子进程1',1))
#     p2=Process(target=task,args=('子进程2',2))
#     p3=Process(target=task,args=('子进程3',3))
#
#     start_time=time.time()
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p3.join()
#     p1.join()
#     p2.join()
#
#     stop_time=time.time()
#     print('主',(stop_time-start_time))


# from multiprocessing import Process
# import time
#
# def task(name,n):
#     print('%s is running ' %name)
#     time.sleep(n)
#     print('%s is done ' % name)
#
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=('子进程1',1))
#     p2=Process(target=task,args=('子进程2',2))
#     p3=Process(target=task,args=('子进程3',3))
#
#     start=time.time()
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#
#     stop=time.time()
#     print('主',(stop-start))


# from multiprocessing import Process
# import time
#
# def task(name,n):
#     print('%s is running ' %name)
#     time.sleep(n)
#     print('%s is done ' % name)
#
#
# if __name__ == '__main__':
#     # p1=Process(target=task,args=('子进程1',1))
#     # p1.start()
#     # p2=Process(target=task,args=('子进程2',2))
#     # p2.start()
#     # p3=Process(target=task,args=('子进程3',3))
#     # p3.start()
#
#     p_l=[]
#     start=time.time()
#     for i in range(1,4):
#         p=Process(target=task,args=('子进程%s' %i,i))
#         p_l.append(p)
#         p.start()
#
#     # print(p_l)
#     for p in p_l:
#         p.join()
#
#     stop=time.time()
#
#     print('主',(stop-start))



# pid
# from multiprocessing import Process
# import time
# import os
#
# def task(n):
#     print('%s is running ' %os.getpid())
#     time.sleep(n)
#     print('%s is done ' % os.getpid())
#
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(10,))
#     # print(p1.pid)
#     p1.start()
#     print(p1.pid) # 父进程内查看子pid的方式
#     print('主')


from multiprocessing import Process
import time
import os

def task():
    print('自己的id：%s 父进程的id：%s ' %(os.getpid(),os.getppid()))
    time.sleep(200)

if __name__ == '__main__':
    p1=Process(target=task)
    p1.start()
    print('主',os.getpid(),os.getppid())
    # 爹=》主--》儿子





# 了解
# from multiprocessing import Process,current_process
# import time
#
# def task():
#     print('子进程[%s]运行。。。。' %current_process().name)
#     time.sleep(200)
#
# if __name__ == '__main__':
#     p1=Process(target=task,name='子进程1')
#     p1.start()
#     # print(p1.name)
#     print('主')




# from multiprocessing import Process,current_process
# import time
#
# def task():
#     print('子进程[%s]运行。。。。' %current_process().name)
#     time.sleep(2)
#
# if __name__ == '__main__':
#     p1=Process(target=task,name='子进程1')
#     p1.start()
#
#     # print(p1.is_alive())
#     # p1.join()
#     # print(p1.is_alive())
#
#     p1.terminate()
#     time.sleep(1)
#     print(p1.is_alive())
#     print('主')
