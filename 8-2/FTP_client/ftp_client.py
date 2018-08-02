import optparse
import socket
import configparser    #文件配置
import json


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
        self.authenticate()



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
            print(STATUS_CODE[254])
        else:
            print(STATUS_CODE[response['status_code']])





ch = ClientHandler()

ch.ineractive()




