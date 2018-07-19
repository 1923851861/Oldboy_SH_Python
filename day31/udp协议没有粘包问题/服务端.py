import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #数据报协议-》udp
server.bind(('127.0.0.2',808))

data,client_addr=server.recvfrom(1) #b'hello'==>b'h'
print('第一次：',client_addr,data)

data,client_addr=server.recvfrom(1024) #b'world' =>b'world'
print('第二次：',client_addr,data)
#
data,client_addr=server.recvfrom(1024)
print('第三次：',client_addr,data)

server.close()