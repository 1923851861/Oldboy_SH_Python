from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

conn,addr=server.accept()

res1=conn.recv(1024)
print('第一次；',res1)

res2=conn.recv(1024)
print('第二次；',res2)

res3=conn.recv(1024)
print('第三次；',res3)