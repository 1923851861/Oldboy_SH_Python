import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #数据报协议-》udp

client.sendto('hello'.encode('utf-8'),('127.0.0.2',808))
client.sendto('world'.encode('utf-8'),('127.0.0.2',808))
client.sendto(''.encode('utf-8'),('127.0.0.2',808))

client.close()