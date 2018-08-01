from socket import *
ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
while True:
    msg = input('>>>>>:').strip()
    if not msg:continue
    tcp_client.send(msg.encode('utf8'))
    data = tcp_client.recv(buffer_size)
    print('服务器端：', data.decode('utf8'))