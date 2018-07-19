import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        #通信循环
        # print(self.client_address)
        # print(self.request)

        data=self.request[0]
        print('客户消息',data)
        self.request[1].sendto(data.upper(),self.client_address)


if __name__ == '__main__':
    s=socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyHandler)
    s.serve_forever()