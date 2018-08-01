'''
UDP没有连接,可以实现并发

如果收到消息缓冲区里的数据为空，recvfrom不会阻塞
recvfrom收的数据小鱼sendinto发送的 数据是，数据丢失
只有sendto发送数据没有recvfrom收数据，数据丢失

单独运行UDP客户端不会报错，而TCP会报错，因为UDP只负责发包，不管有没有接受，TCP基于链接，必须建立连接才能传递消息

UDP的recvfrom是阻塞的，一个recvfrom（x）必须对一个一个sendinto（y），收完了x字节的数据就算完成，若是y》x数据就丢失，以为这UDP不会粘包，但会丢失数据，不可靠
TCP协议数据不会丢失，己端总是在收到ack时才会清除缓冲区内容，数据时可靠的，但是会粘包


'''



# from  socket import *
# ip_port = ('172.24.36.5',8000)
# buffer_size = 1021
#
# udp_sever = socket(AF_INET,SOCK_DGRAM)  #SOCK_DGRAM数据包式套接字
# udp_sever.bind(ip_port)
#
# while True:
#     data = udp_sever.recvfrom(buffer_size)
#     print(data)   #(b'HelloWorld', ('172.24.36.5', 57162))
#
#

from  socket import *
ip_port = ('172.24.36.5',8000)
buffer_size = 1021

udp_sever = socket(AF_INET,SOCK_DGRAM)  #SOCK_DGRAM数据包式套接字
udp_sever.bind(ip_port)

while True:
    data,addr= udp_sever.recvfrom(buffer_size)
    print(data.decode('utf8'))
    msg = input('>>>>>:')
    udp_sever.sendto(msg.encode('utf8'),addr)








