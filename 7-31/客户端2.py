from socket import *

ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1021

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

tcp_client.send('Heloo World!'.encode('utf8'))



print('客户端已经发送消息！')
data = tcp_client.recv(buffer_size)
print('收到服务器端发来的消息是--------->',data.decode('utf8'))

tcp_client.close()
