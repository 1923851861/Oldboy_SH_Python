from threading import Timer,current_thread


def task(x):
    print('%s run....' %x)
    print(current_thread().name)


if __name__ == '__main__':
    t=Timer(3,task,args=(10,))
    t.start()
    print('主')