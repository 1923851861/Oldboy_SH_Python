import socket

#1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp称为流式协议,udp称为数据报协议SOCK_DGRAM
# print(phone)

#2、插入/绑定手机卡
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8080))

#3、开机
phone.listen(5) # 半连接池，限制的是请求数

#4、等待电话连接
print('start....')
conn,client_addr=phone.accept() #（三次握手建立的双向连接，（客户端的ip，端口））
# print(conn)
print(client_addr)

#5、通信：收\发消息
data=conn.recv(1024) #最大接收的字节数
print('来自客户端的数据',data)
conn.send(data.upper())


# import time
# time.sleep(500)
#6、挂掉电话连接
conn.close()

#7、关机
phone.close()
















