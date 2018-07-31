from socket import *
import subprocess

ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)


while True:
    cmd = input('>>>:').strip()
    if not cmd:continue
    if cmd == 'quit':break

    tcp_client.send(cmd.encode('utf-8'))
    cmd_res = tcp_client.recv(buffer_size)
    print('命令的执行结果是：',cmd_res.decode('gbk'))
tcp_client.close()

