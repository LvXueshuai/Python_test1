
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        print('收到消息为：',self.request[0])
        self.request[1].sendto(self.request[0].upper(),self.client_address) #self.client_address为地址





#多线程方式解决并发
if __name__ == '__main__':
    s = socketserver.ThreadingUDPServer(('172.24.36.5',8000),MyServer)    #多线程TCP服务
    s.serve_forever()  #永远服务








