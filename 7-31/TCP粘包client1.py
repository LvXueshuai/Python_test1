from socket import *


ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

tcp_client.send('helloWorldHaha'.encode('utf8'))
# tcp_client.send('world'.encode('utf8'))
# tcp_client.send('hah'.encode('utf8'))





tcp_client.close()
