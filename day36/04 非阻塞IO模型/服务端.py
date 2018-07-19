from socket import *
import time

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.2',808))
server.listen(5)
server.setblocking(False)

conn_l=[]   #创建连接数空列表
while True:
    try:
        print('总连接数[%s]' % len(conn_l))
        conn,addr=server.accept()
        conn_l.append(conn)
    except BlockingIOError:
        del_l=[]    #创建捕捉异常空列表
        for conn in conn_l:
            try:
                data=conn.recv(1024)
                if len(data) == 0:
                    del_l.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except ConnectionResetError:
               del_l.append(conn)

        for conn in del_l:
            conn_l.remove(conn)