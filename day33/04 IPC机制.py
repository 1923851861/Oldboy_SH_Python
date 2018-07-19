#IPC：进程间通信，有两种实现方式
#1、pipe：
#2、queue：pipe+锁


from multiprocessing import Queue
#
#
# q=Queue(3) #先进先出
# # 注意：
# # 1、队列占用的是内存空间
# # 2、不应该往队列中放大数据，应该只存放数据量较小的消息
# # 掌握的
# q.put('first')
# q.put({'k':'sencond'})
# q.put(['third',])
# # q.put(4)
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
#

#了解的
# q=Queue(3) #先进先出
# q.put('first',block=True,timeout=3)
# q.put({'k':'sencond'},block=True,timeout=3)
# q.put(['third',],block=True,timeout=3)
# print('===>')
# # q.put(4,block=True,timeout=3)
#
#
# print(q.get(block=True,timeout=3))
# print(q.get(block=True,timeout=3))
# print(q.get(block=True,timeout=3))
# print(q.get(block=True,timeout=3))



# q=Queue(3) #先进先出
# q.put('first',block=False,)
# q.put({'k':'sencond'},block=False,)
# q.put(['third',],block=False,)
# print('===>')
# # q.put(4,block=False,) # 队列满了直接抛出异常，不会阻塞
#
# print(q.get(block=False))
# print(q.get(block=False))
# print(q.get(block=False))
# print('get over')
# print(q.get(block=False))
#


q=Queue(3) #先进先出

q.put_nowait('first') #q.put('first',block=False,)
q.put_nowait(2)
q.put_nowait(3)
# q.put_nowait(4)

print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())
