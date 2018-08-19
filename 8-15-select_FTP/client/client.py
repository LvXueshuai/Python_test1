import socket
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class selectFtpClient():
    def __init__(self):
        self.hasReceived = 0
        self.args = sys.argv   #sys.argv是命令行输入的参数。第一个为默认文件名，后边为跟的
        if len(self.args) > 1:
            port = (self.args[1],int(self.args[2]))
        else:
            port = ('127.0.0.1',8885)  #server端
        self.creat_socket(port)
        self.command_fanout()

    def creat_socket(self,port):   #创建连接
        try:
            self.sk = socket.socket()
            self.sk.connect(port)
            print('连接服务器成功......')
        except Exception as e:
            print('Error:',e)

    def command_fanout(self):   #发送消息
        while True:
            cmd = input('>>>').strip()      #put a.avi
            if cmd == 'exit()':
                break
            cmd,file = cmd.split()
            if hasattr(self,cmd):
                func = getattr(self,cmd)
                func(cmd,file)             #put('put','a.avi')
            else:
                print('调用错误')

    def put(self,cmd,file):
        if os.path.isfile(file):
            fileName = os.path.basename(file)
            fileSize = os.path.getsize(file)
            fileInfo = '%s|%s|%s' %(cmd,fileName,fileSize)
            self.sk.send(bytes(fileInfo,encoding='utf8'))
            recvStatus = self.sk.recv(1024)
            print('recvStatus:',recvStatus)
            hasSend = 0
            if str(recvStatus,encoding='utf8') == 'OK':
                with open(file,'rb') as f:
                    while fileSize > hasSend:
                        contant = f.read(1024)
                        recv_size = len(contant)
                        self.sk.send(contant)
                        hasSend += recv_size
                        s = str(int(hasSend/fileSize*100))+'%'
                        print('正在上传：'+fileName+' 已经上传：'+s)
                print('%s文件上传完毕' %(fileName,))
        else:
            print('文件不存在！')


    def get(self,cmd,file):
        # fileName = os.path.basename(file)
        fileName = file
        filesize = 0
        fileInfo = '%s|%s|%s' % (cmd,fileName,filesize)
        self.sk.send(bytes(fileInfo, encoding='utf8'))

        # recvStatus = self.sk.recv(1024)
        # print('RecvStatus:', recvStatus)

        data = self.sk.recv(1024).decode('utf8')

        Num,fileSize = str(data).split('|')


        if Num == 'YES':
            self.sk.send('sdgs'.encode('utf8'))

            path = os.path.join(BASE_DIR,fileName)


            with open(path, 'ab') as f:
                recv_data = self.sk.recv(int(fileSize))
                self.hasReceived += len(recv_data)
                f.write(recv_data)
                print(self.hasReceived)
                # s = str(int(self.hasReceived / fileSize * 100)) + '%'
                # print('正在下载：' + fileName + ' 已经下载：' + s)
                print('%s下载完毕' % fileName)

        else:
            print('下载文件不存在！')



if __name__ == '__main__':

    selectFtpClient()
