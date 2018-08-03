import optparse
import socket
import configparser    #文件配置
import json
import os,sys


STATUS_CODE = {
    254:'Passed authentication',
    253:'NO'
}


class ClientHandler():

    def __init__(self):
        self.op = optparse.OptionParser()

        self.op.add_option('-s','--server',dest = 'server')
        self.op.add_option('-P', '--port', dest='port')
        self.op.add_option('-u', '--username', dest='username')
        self.op.add_option('-p', '--password', dest='password')

        self.options,self.args = self.op.parse_args()

        self.verify_args(self.options,self.args)
        self.make_connection()
        self.mainPath = os.path.dirname(os.path.abspath(__file__))
        self.last = 0

    def verify_args(self,options,args):

        port = options.port


        if int(port) > 0 and int(port) < 65535:
            return True

        else:
            exit('PORT IS IN 0-65535')

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server,int(self.options.port)))

    def ineractive(self):
        print('Begin To Interactive......')

        if self.authenticate():

            cmd_info = input('【%s】'%self.current_dir).strip()
            cmd_list = cmd_info.split()

            if hasattr(self,cmd_list[0]):   #反射
                func = getattr(self,cmd_list[0])
                func(*cmd_list)

    def put(self,*cmd_list):

        action,local_path,target_path = cmd_list
        local_path = os.path.join(self.mainPath,local_path)

        file_name = os.path.basename(local_path)
        file_size = os.stat(local_path).st_size

        data = {
            'action':'put',
            'file_name':file_name,
            'file_size':file_size,
            'target_path':target_path
        }

        self.sock.send(json.dumps(data).encode('utf8'))

        is_exist = self.sock.recv(1024).decode('utf8')

        has_sent = 0
        if is_exist == '800':
            # 文件不完整
            choice = input('文件已存在，但不完整，是否继续上传？[Y/N]').strip()
            if choice.upper() == 'Y':
                self.sock.send('Y'.encode('utf8'))
                continue_position = self.response(1024)
                has_sent += int(continue_position)

            else:
                self.sock.send('N'.encode('utf8'))

        elif is_exist == '801':
            #文件完全存在
            print('该文件已存在！')
            return

        else:
            pass

        f = open(local_path,'rb')
        f.seek(has_sent)
        while has_sent < file_size:
            data = f.read(1024)
            self.sock.sendall(data)
            has_sent += len(data)
            self.show_progress(has_sent,file_size)

        f.close()
        print('上传成功')

    def show_progress(self,has,total):   #进度条
        rate = float(has)/float(total)
        rate_number = int(rate * 100)
        # if self.last != rate_number:
        #     sys.stdout.write('%s%% %s\r' %(rate_number,'#'*rate_number))
        # self.last = rate_number
        sys.stdout.write('%s%% %s\r' % (rate_number, '#' * rate_number))

    def ls(self,*cmd_list):
        data = {
            'action':'ls',
        }
        self.sock.sendall(json.dumps(data).encode('utf8'))

        data = self.sock.recv(1024).decode('utf8')
        print(data)

    def cd(self, *cmd_list):
        data = {
            'action': 'cd',
            'dirname':cmd_list[1],

        }
        self.sock.sendall(json.dumps(data).encode('utf8'))

        data = self.sock.recv(1024).decode('utf8')
        print(os.path.basename(data))
        self.current_dir = os.path.basename(data)  #显示为当前文件夹名称


    def mkdir(self, *cmd_list):
        data = {
            'action':'mkdir',
            'dirname':cmd_list[1],
        }
        self.sock.sendall(json.dumps(data).encode('utf8'))
        data = self.sock.recv(1024).decode('utf8')
        print(data)


    def authenticate(self):

        if self.options.username is None or self.options.password is None:
            username = input('username:')
            password = input('password:')
            return self.get_auth_result(username,password)

        return self.get_auth_result(self.options.username,self.options.password)

    def response(self):
        data = self.sock.recv(1024).decode('utf8')
        data = json.loads(data)
        return data


    def get_auth_result(self,user,pwd):

        data = {
            "action":"auth",
            "username":user,
            "password":pwd
        }

        self.sock.send(json.dumps(data).encode('utf8'))





        response = self.response()
        print('RESPONSE:',response['status_code'])
        if response['status_code'] ==254:
            self.user = user
            self.current_dir = user
            print(STATUS_CODE[254])
            return True
        else:
            print(STATUS_CODE[response['status_code']])





ch = ClientHandler()

ch.ineractive()




