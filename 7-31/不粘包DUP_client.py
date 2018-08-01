from  socket import *
ip_port = ('172.24.36.5',8000)
buffer_size = 1021

udp_client = socket(AF_INET,SOCK_DGRAM)

udp_client.sendto('hello'.encode('utf8'),ip_port)
udp_client.sendto('world'.encode('utf8'),ip_port)
udp_client.sendto('haha'.encode('utf8'),ip_port)