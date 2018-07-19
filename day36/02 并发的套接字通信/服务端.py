from gevent import spawn,monkey;monkey.patch_all()
from socket import *
from threading import Thread

def talk(conn):
    while True:
        try:
            data=conn.recv(1024)
            if len(data) == 0:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()

def server(ip,port,backlog=5):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(backlog)

    print('starting...')
    while True:
        conn, addr = server.accept()
        spawn(talk, conn,)

if __name__ == '__main__':
    g=spawn(server,'127.0.0.1',8080)
    g.join()
