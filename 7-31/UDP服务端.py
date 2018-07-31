'''
UDP没有连接,可以实现并发

'''



# from  socket import *
# ip_port = ('172.24.36.5',8000)
# buffer_size = 1021
#
# udp_sever = socket(AF_INET,SOCK_DGRAM)  #SOCK_DGRAM数据包式套接字
# udp_sever.bind(ip_port)
#
# while True:
#     data = udp_sever.recvfrom(buffer_size)
#     print(data)   #(b'HelloWorld', ('172.24.36.5', 57162))
#
#

from  socket import *
ip_port = ('172.24.36.5',8000)
buffer_size = 1021

udp_sever = socket(AF_INET,SOCK_DGRAM)  #SOCK_DGRAM数据包式套接字
udp_sever.bind(ip_port)

while True:
    data,addr= udp_sever.recvfrom(buffer_size)
    print(data.decode('utf8'))
    msg = input('>>>>>:')
    udp_sever.sendto(msg.encode('utf8'),addr)








