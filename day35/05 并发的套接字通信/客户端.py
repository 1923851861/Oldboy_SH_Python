from socket import *
import os

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.2',8081))

while True:
    msg='%s say hello' %os.getpid()
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)
    print(data.decode('utf-8'))