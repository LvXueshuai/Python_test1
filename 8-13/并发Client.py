import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8801))

while True:
    inp = input('>>>')
    sk.sendall(bytes(inp,'utf8'))
    data = sk.recv(1024)
    print(str(data,'utf8'))