'''
UDP没有粘包现象
'''


from socket import *
import subprocess

ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

udp_sever = socket(AF_INET,SOCK_DGRAM)
udp_sever.bind(ip_port)


while True:
    cmd,addr = udp_sever.recvfrom(buffer_size)

    res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE)
    err = res.stderr.read()
    if err:
        cmd_res = err
    else:
        cmd_res = res.stdout.read()

    if not cmd_res:
        cmd_res = 'Success'.encode('gbk')

    udp_sever.sendto(cmd_res,addr)
