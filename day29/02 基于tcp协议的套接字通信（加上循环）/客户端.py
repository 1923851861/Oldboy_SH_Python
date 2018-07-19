import socket

#1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(phone)
#2、拨电话
phone.connect(('127.0.0.1',8080)) # 指定服务端ip和端口

#3、通信：发\收消息
while True: # 通信循环
    msg=input('>>: ').strip() #msg=''
    if len(msg) == 0:continue
    phone.send(msg.encode('utf-8'))
    # print('has send----->')
    data=phone.recv(1024)
    # print('has recv----->')
    print(data)

#4、关闭
phone.close()