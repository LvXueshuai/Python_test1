'''
IO多路复用：      单线程下实现并发
    select   （效率最低）最大监听量有限   跨平台，都存在
    poll
    epoll    （最好）

'''


import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1',8801))
sk.listen(5)
inputs = [sk,]
while True:
    r,w,e = select.select(inputs,[],[],5)   #5为默认等待时间
    # print(len(r))

    for obj in r:
        if obj == sk:
            conn,addr = obj.accept()
            print(conn)
            inputs.append(conn)
        else:
            data_bye = obj.recv(1024)
            print(str(data_bye,'utf8'))
            inp = input('回答%s号客户》》》' %inputs.index(obj))
            obj.sendall(bytes(inp,'utf8'))
    print('》》》',r)