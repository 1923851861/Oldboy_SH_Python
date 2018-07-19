from multiprocessing import Process
import time

x=100
def task():
    global x
    x=0
    print('done')
if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    time.sleep(5) # 让父进程在原地等待，等了500s后，才执行下一行代码
    print(x)