from threading import Thread
import time

#方式一
def task(name):
    print('%s is running' %name)
    time.sleep(3)
    print('%s is done' %name)
if __name__ == '__main__':
    t=Thread(target=task,args=('子线程',))
    t.start()
    print('主')


#方式二
# class Mythread(Thread):
#     def run(self):
#         print('%s is running' %self.name)
#         time.sleep(3)
#         print('%s is done' %self.name)
#
# if __name__ == '__main__':
#     t=Mythread()
#     t.start()
#     print('主')
