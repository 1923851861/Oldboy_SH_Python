from socket import *
import subprocess
import struct
import json

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.3',8088))
server.listen(5)

while True:
    conn,client_addr=server.accept()
    print('新的客户端',client_addr)

    while True:
        try:
            cmd=conn.recv(1024) #cmd=b'dir'
            if len(cmd) == 0:break

            # 运行系统命令
            obj=subprocess.Popen(cmd.encode('utf-8'),
                             shell=True,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE
                             )

            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            #先制作报头
            header_dic={
                'filename':'a.txt',
                'total_size':len(stdout) + len(stderr),
                'hash':'xasf123213123'
            }
            header_json=json.dumps(header_dic)
            header_bytes=header_json.encode('utf-8')

            #1、先把报头的长度len(header_bytes)打包成4个bytes，然后发送
            conn.send(struct.pack('i',len(header_bytes)))
            #2、发送报头
            conn.send(header_bytes)
            #3、再发送真实的数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()