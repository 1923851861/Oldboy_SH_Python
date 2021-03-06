from threading import Thread,Lock
import time

mutex=Lock()
n=100

def task():
    global n
    with mutex:
        temp=n
        time.sleep(0.1)
        n=temp-1

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