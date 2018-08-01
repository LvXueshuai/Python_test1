
from  socket import *
ip_port = ('172.24.36.5',8000)
buffer_size = 1021

udp_sever = socket(AF_INET,SOCK_DGRAM)  #SOCK_DGRAM数据包式套接字
udp_sever.bind(ip_port)

data1 = udp_sever.recvfrom(1024)
print('消息1为', data1)
data2 = udp_sever.recvfrom(5)
print('消息2为', data2)
data3= udp_sever.recvfrom(1)  #OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。
print('消息3为', data3)



