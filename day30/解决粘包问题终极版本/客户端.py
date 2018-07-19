from socket import *
import struct
import json

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.3',8088))

while True:
    cmd=input('>>: ').strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))

    #1、先收4个字节，该4个字节中包含报头的长度
    header_len=struct.unpack('i',client.recv(4))[0]

    #2、再接收报头
    header_bytes=client.recv(header_len)

    #从报头中解析出想要的内容
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    print(header_dic)
    total_size=header_dic['total_size']

    #3、再收真实的数据
    recv_size=0
    res=b''
    while recv_size < total_size :
        data=client.recv(1024)
        res+=data
        recv_size+=len(data)

    print(res.decode('gbk'))