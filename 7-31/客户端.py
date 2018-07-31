import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8000)) #拨通电话

phone.send('Rfdsd'.encode('utf8'))

data = phone.recv(2048)

print('收到服务器端发送的消息为',data)
