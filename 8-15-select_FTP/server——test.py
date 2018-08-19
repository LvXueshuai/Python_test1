import socket

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8055))
    sock.listen(5)

    while True:
        conn,addr = sock.accept()
        buf = conn.recv(1024)

        f = open('test.html','rb')
        data = f.read()


        conn.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n','utf8'))   # IE浏览器必须
        conn.sendall(data)
        # conn.sendall(bytes('<h1>Hello</h1>','utf8'))

        conn.close()

if __name__ == '__main__':
    main()