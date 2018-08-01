
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):

        print('COON IS',self.request)  #conn
        print('ADDR IS',self.client_address)   #addr

        while True:
            try:
                data = self.request.recv(1024)
                if not data:break
                print('收到的消息：',data,self.client_address)

                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break


#多线程方式解决并发
if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('172.24.36.5',8000),MyServer)    #多线程TCP服务
    s.serve_forever()  #永远服务








