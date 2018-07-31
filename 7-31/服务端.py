import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#网络通信基于TCP  流式链接
# AF_INET代表基于网络类型的套接字   SOCK_STREAM代表TCP协议

phone.bind(('127.0.0.1',8000))  #IP地址+端口

phone.listen(5)  #表示最多有5个等待
print('正在等电话')
conn,addr =phone.accept()  #等电话    链接，手机号（地址）

msg = conn.recv(1024) #收消息
print('客户端发来的消息是:',msg)

conn.send(msg.upper())#发消息

conn.close()

phone.close()