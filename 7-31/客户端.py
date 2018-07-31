import socket

ip_port = ('172.24.36.5',8000)
buffer_size = 1021

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# phone.connect(('127.0.0.1',8000)) #拨通电话    本机
# phone.connect(('172.24.36.29',8000)) #拨通电话
phone.connect(ip_port) #拨通电话

phone.send('Rfdsd'.encode('utf8'))

data = phone.recv(buffer_size)

print('收到服务器端发送的消息为',data)
