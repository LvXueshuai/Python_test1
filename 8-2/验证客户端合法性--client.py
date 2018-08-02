
__auther__ = 'lxs'
from socket import *
import hmac,os

secert_key = b'lvxueshuai'



def clien_handler(ip_port,bufsize = 1024):
    tcp_socke_client = socket(AF_INET,SOCK_STREAM)
    tcp_socke_client.connect(ip_port)

    conn_auth(tcp_socke_client)
    while True:
        data = input('>>:').strip()
        if not data:continue

        tcp_socke_client.sendall(data.encode('utf8'))
        respone = tcp_socke_client.recv(bufsize)
        print('服务器返回的消息为【%s】' %(respone.decode('utf8')))
    tcp_socke_client.close()


def conn_auth(conn):
    '''
    验证链接
        :param conn:
    :return:
    '''
    msg = conn.recv(48)
    h = hmac.new(secert_key,msg)
    digest = h.digest()
    conn.sendall(digest)


if __name__ == '__main__':
    ip_port = ('172.24.36.5',8000)
    bufsize = 1024
    clien_handler(ip_port,bufsize)
