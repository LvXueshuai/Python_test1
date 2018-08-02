#_*_coding:utf-8_*_
__auther__ = 'lxs'

from socket import *
import hmac,os

secert_key = b'lvxueshuai'

def conn_auth(conn):
    '''
    认证客户端链接
    :param conn:
    :return:
    '''
    print('开始认证客户端合法性-->')
    msg = os.urandom(48)
    conn.sendall(msg)
    h = hmac.new(secert_key,msg)
    digest = h.digest()
    respone = conn.recv(len(digest))
    return hmac.compare_digest(digest,respone)

def data_handler(conn,bufsize = 1024):
    if not conn_auth(conn):

        conn.close()
        print('链接不合法,已关闭！')
        return

    print('链接合法,开始通信！')
    while True:
        data = conn.recv(bufsize)
        if not data:break
        print('客户端发来的消息为【%s】' %(data.decode('utf8')))
        conn.sendall(data.upper())

def server_handler(ip_port,bufsize,backlog = 5):
    '''
    只处理链接
    :param ip_port: 
    :param bufsize: 
    :param backlog: 
    :return: 
    '''
    tcp_socket_server = socket(AF_INET,SOCK_STREAM)
    tcp_socket_server.bind(ip_port)
    tcp_socket_server.listen(backlog)
    while True:
        conn,addr = tcp_socket_server.accept()
        print('新链接【%s,%s】' %(addr[0],addr[1]))
        data_handler(conn,bufsize)
if __name__ == '__main__':
    ip_port = ('172.24.36.5',8000)
    bufsize = 1024
    server_handler(ip_port,bufsize)



