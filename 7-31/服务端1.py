# import socket
#
# tcp_sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

from socket import *

ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1021

tcp_sever = socket(AF_INET,SOCK_STREAM)
tcp_sever.bind(ip_port)
tcp_sever.listen(back_log)

conn,addr = tcp_sever.accept()
print('双向链接是',conn)
print('客户端地址是：',addr)

data = conn.recv(buffer_size)
print('客户端发来的消息是：',data)
conn.send(data.upper())

conn.close()
tcp_sever.close()
