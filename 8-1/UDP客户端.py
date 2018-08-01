from  socket import *
ip_port = ('172.24.36.5',8000)
buffer_size = 1021

udp_client = socket(AF_INET,SOCK_DGRAM)  #SOCK_DGRAM数据包式套接字
while True:
    msg = input('>>>>>:').strip()
    udp_client.sendto(msg.encode('utf8'),ip_port)

    data, addr = udp_client.recvfrom(buffer_size)
    print(data.decode('utf8'))