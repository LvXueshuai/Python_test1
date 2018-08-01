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

    # data1 = conn.recv(buffer_size)
    #
    # print('消息1为', data1)
    #
    # data2 = conn.recv(buffer_size)
    #
    # print('消息2为', data2)
    #
    # data3 = conn.recv(buffer_size)
    #
    # print('消息3为', data3)

    data1 = conn.recv(5)

    print('消息1为', data1)

    data2 = conn.recv(5)

    print('消息2为', data2)

    data3 = conn.recv(5)

    print('消息3为', data3)


tcp_sever.close()