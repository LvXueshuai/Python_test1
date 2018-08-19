import selectors
import socket

sel =selectors.DefaultSelector()   #根据操作系统自动选择

def accept(sock,nask):
    conn,addr = sock.accept()
    print('Acceped',conn,'from',addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    try:
        data = conn.recv(1000)
        if not data:
            raise Exception
        print('Echoing', repr(data), 'to', conn)
        conn.send(data)
    except Exception as e:

        print('Closing',conn)
        sel.unregister(conn)
        conn.close()

sock =socket.socket()
sock.bind(('localhost',8090))
sock.listen(100)
sock.setblocking(False)

sel.register(sock,selectors.EVENT_READ,accept)   #注册，， 将sock与accept邦洞
print('Server....')
while True:

    events = sel.select()
    for key,mask in events:

        # print('key',key)
        # print('mask',mask)
        callback = key.data
        # print('Callback',callback)
        callback(key.fileobj,mask)



