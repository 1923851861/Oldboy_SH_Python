import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080)) # 指定服务端ip和端口

while True: 
    # msg=input('>>: ').strip() #msg=''
    msg = 'client22222'  # msg=''
    if len(msg) == 0:continue
    phone.send(msg.encode('utf-8'))
    data=phone.recv(1024)
    print(data)


phone.close()