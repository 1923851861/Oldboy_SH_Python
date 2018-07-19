import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        #通信循环
        while True:
            # print(self.client_address)
            # print(self.request) #self.request=conn

            try:
                data=self.request.recv(1024)
                if len(data) == 0:break
                self.request.send(data.upper())
            except ConnectionResetError:
                break


if __name__ == '__main__':
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyHandler,bind_and_activate=True)

    s.serve_forever()  # 代表连接循环
    # 循环建立连接，每建立一个连接就会启动一个线程（服务员）+调用Myhanlder类产生一个对象，调用该对象下的handle方法，专门与刚刚建立好的连接做通信循环