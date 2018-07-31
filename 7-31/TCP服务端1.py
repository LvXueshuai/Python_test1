# import socket
#
# tcp_sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

from socket import *

ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

tcp_sever = socket(AF_INET,SOCK_STREAM)
tcp_sever.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  #加入一条socket配置，重用ip和端口
tcp_sever.bind(ip_port)
tcp_sever.listen(back_log)
while True:   #长久运行
    conn,addr = tcp_sever.accept()
    print('双向链接是',conn)
    print('客户端地址是：',addr)

    while True:
        try:
            data = conn.recv(buffer_size)
            print('客户端：',data.decode('utf8'))
            msg = input('>>>>>:')
            if not msg: continue
            conn.send(msg.encode('utf8'))
            print('服务器端：',msg)
        except Exception:
            break
    conn.close()
tcp_sever.close()
