import queue

# 队列:先进先出
q=queue.Queue(3)
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())

# 堆栈：先进后出
q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())

# 优先级队列：优先级高先出来,数字越小，优先级越高
q=queue.PriorityQueue()
q.put((3,'data1'))
q.put((-10,'data2'))
q.put((11,'data3'))

print(q.get())
print(q.get())
print(q.get())
