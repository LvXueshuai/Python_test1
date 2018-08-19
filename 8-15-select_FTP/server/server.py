import os
import time
import socket
import selectors
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class selecFtpServer:
    def __init__(self):
        self.dic = {}
        self.hasSend = 0
        self.hasReceived = 0
        self.sel =selectors.DefaultSelector()   #实例对象
        self.create_socket()
        self.handle()

    def create_socket(self):   #创建socket对象
        '''
        绑定，监听
        :return:
        '''
        server = socket.socket()
        server.bind(('127.0.0.1',8885))
        server.listen(5)
        server.setblocking(False)
        self.sel.register(server,selectors.EVENT_READ,self.accept)   #相当于把server当做参数传入accept



    def handle(self):
        while True:
            events = self.sel.select()  #监听  1.[srever,]            2.[server,conn1]
            for key,mask in events:
                callback = key.data     #      1.self.accept(server)  2.self.read(conn1)
                callback(key.fileobj,mask)  #1. key.fileobj = server  2.key.fileobj = conn1

    def accept(self,sock,mask):

        conn,addr = sock.accept()
        print('from %s %s conneced' %addr)

        self.sel.register(conn,selectors.EVENT_READ,self.read)
        conn.setblocking(False)
        self.dic[conn] = {}

    def read(self,conn,mask):
        try:
            if not self.dic[conn]:   #判断是否是第一次
                print('---------111111----------')
                data = conn.recv(1024)
                cmd,filename,filesize = str(data,encoding='utf8').split('|')
                self.dic = {conn:{'cmd':cmd,'filename':filename,'filesize':int(filesize)}}

                if cmd == 'put':
                    conn.send(bytes('OK',encoding='utf8'))

                if self.dic[conn]['cmd'] == 'get':

                    file = os.path.join(BASE_DIR,'download',filename)

                    if os.path.exists(file):
                        fileSize = os.path.getsize(file)
                        self.dic = {conn: {'cmd': cmd, 'filename': filename, 'filesize': int(fileSize)}}
                        send_info = '%s|%s' %('YES',fileSize)

                        conn.send(bytes(send_info.encode('utf8')))
                    else:
                        send_info = '%s|%s' %('NO',0)
                        conn.send(bytes(send_info,encoding='utf8'))
            else:
                if self.dic[conn].get('cmd',None):
                    print('-----------222222222222222222-------------')
                    cmd = self.dic[conn].get('cmd')

                    if hasattr(self,cmd):
                        func = getattr(self,cmd)
                        print('-----------3333333333----------')
                        func(conn)
                    else:
                        print('Error cmd nei!')
                        conn.close()
                else:
                    print('Error cmd wai!')
                    conn.close()

        except Exception as e:
            print('Error:',e)
            self.sel.unregister(conn)
            conn.close()

    def put(self,conn):
        fileName = self.dic[conn]['filename']
        fileSize = self.dic[conn]['filesize']
        path = os.path.join(BASE_DIR,'upload',fileName)
        recv_data = conn.recv(10240)
        self.hasReceived += len(recv_data)

        with open(path,'ab') as f:
            f.write(recv_data)
        if fileSize == self.hasReceived:
            if conn in self.dic.keys():
                self.dic[conn] = {}
            print('%s上传完毕' %fileName)

    def get(self,conn):
        print('get')
        fileName = self.dic[conn]['filename']
        file = os.path.join(BASE_DIR, 'download', fileName)
        fileSize = os.path.getsize(file)


        # with open(file, 'rb') as f:
        #     while fileSize > self.hasSend:
        #         contant = f.read(1024)
        #         recv_size = len(contant)
        #         conn.send(contant)
        #         self.hasSend += recv_size
        #
        # print('%s文件传输完毕' % (fileName,))

        with open(file, 'rb') as f:


            contant = f.read(fileSize)
            recv_size = len(contant)
            conn.send(contant)
            self.hasSend += recv_size

        print('%s文件传输完毕' % (fileName,))







if __name__ == '__main__':
    selecFtpServer()