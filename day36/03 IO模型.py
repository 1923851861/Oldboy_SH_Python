
'''
网络IO：
    recvfrom：
        wait data：等待客户端产生数据——》客户端OS--》网络--》服务端操作系统缓存
        copy data：由本地操作系统缓存中的数据拷贝到应用程序的内存中

    send：
        copy data

'''

# conn.recv(1024) ==>OS