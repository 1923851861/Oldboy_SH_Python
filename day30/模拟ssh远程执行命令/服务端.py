from socket import *
import subprocess
import struct

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn,client_addr=server.accept()
    print('新的客户端',client_addr)

    while True:
        try:
            cmd=conn.recv(1024) #cmd=b'dir'
            if len(cmd) == 0:break

            # 运行系统命令
            obj=subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE
                             )

            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            #1、先制作报头（固定长度）
            total_size=len(stdout) + len(stderr)

            header=struct.pack('i',total_size)

            #2、先发送固定长度的报头
            conn.send(header)

            #3、再发送真实的数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()