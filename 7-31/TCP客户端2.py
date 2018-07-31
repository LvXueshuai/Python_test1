from socket import *

import logging
logger = logging.getLogger()   #定义对象方式
fh = logging.FileHandler('test_log',encoding='utf-8')    #向文件发送日志内容
fm = logging.Formatter("%(asctime)s %(filename)s %(lineno)d %(message)s")
fh.setFormatter(fm)
logger.addHandler(fh)
logger.setLevel('DEBUG')   #设置优先级
#--------------------------








ip_port = ('172.24.36.5',8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
while True:
    msg = input('>>>>>:').strip()
    if not msg:continue
    tcp_client.send(msg.encode('utf8'))
    print('客户端：',msg)
    logging.info(msg)
    data = tcp_client.recv(buffer_size)
    print('服务器端：',data.decode('utf8'))
    logging.info(data.decode('utf8'))

tcp_client.close()
