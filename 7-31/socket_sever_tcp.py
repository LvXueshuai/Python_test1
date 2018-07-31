from socket import *
import subprocess

ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

tcp_sever = socket(AF_INET,SOCK_STREAM)
tcp_sever.bind(ip_port)
tcp_sever.listen(back_log)

while True:
    conn,addr = tcp_sever.accept()

    print('新的客户端链接',addr)
    while True:
        #收
        try:
            cmd = conn.recv(buffer_size)
            if not cmd: break
            print('收到客户端的命令：',cmd)
            #执行命令，得到命令的运行结果
            res = subprocess.Popen(cmd.decode('utf-8'),shell = True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()
            #发
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break
