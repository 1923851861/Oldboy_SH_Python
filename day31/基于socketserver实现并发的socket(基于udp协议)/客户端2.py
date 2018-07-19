import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #数据报协议-》udp

while True:
    # msg=input('>>: ').strip() #msg=''
    msg='client2222'
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))
    data,server_addr=client.recvfrom(1024)
    print(data)

client.close()