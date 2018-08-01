from socket import *
import subprocess

ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

udp_client = socket(AF_INET,SOCK_DGRAM)



while True:
    cmd = input('>>>:').strip()
    if not cmd:continue
    if cmd == 'quit':break

    udp_client.sendto(cmd.encode('utf-8'),ip_port)
    cmd_res,addr = udp_client.recvfrom(buffer_size)
    print('命令的执行结果是：',cmd_res.decode('gbk'))
udp_client.close()

