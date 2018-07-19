from socket import *
import struct

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>: ').strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))

    #1、先收固定长度的报头
    header=client.recv(4)

    #2、从报头中解析出对数据的描述信息
    total_size=struct.unpack('i',header)[0]

    #3、再收真实的数据
    recv_size=0
    res=b''
    while recv_size < total_size :
        data=client.recv(1024)
        res+=data
        recv_size+=len(data)

    print(res.decode('gbk'))