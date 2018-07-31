from  socket import *
import time

ip_port = ('172.24.36.5',8000)
buffer_size = 1021

udp_sever = socket(AF_INET,SOCK_DGRAM)  #SOCK_DGRAM数据包式套接字
udp_sever.bind(ip_port)

while True:
    data,addr= udp_sever.recvfrom(buffer_size)
    print(data.decode('utf8'))
    if not data:
        fmt = '%Y-%m-%d %X'
    else:
        fmt = data.decode('utf8')
    # msg = input('>>>>>:')
    # udp_sever.sendto(msg.encode('utf8'),addr)
    back_time = time.strftime(fmt)

    udp_sever.sendto(back_time.encode('utf8'),addr)
