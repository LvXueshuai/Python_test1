#
# import queue
# import multiprocessing
# import random
# import time
#
# def foo(q):
#     time.sleep(1)
#     print('SON:',id(q))
#     q.put([10])
#     q.put(['lxs'])
#     q.put([5])
#
# if __name__ == '__main__':
#     #q = queue.Queue()  #线程队列
#     q = multiprocessing.Queue()  #进程队列
#     p = multiprocessing.Process(target=foo,args=(q,))
#
#     p.start()
#
#     print('MAIN:', id(q))
#     print(q.get())
#     print(q.get())
#     print(q.get())

'''PIPE双向管道实现通信'''
# from multiprocessing import Process
# from multiprocessing import Pipe
#
# def f(conn):
#     conn.send([12,{'name':'lcs'},'hello'])
#     response = conn.recv()
#     print('爸爸说',response)
#     conn.close()
#     print('Q_ID2',id(conn))
#
# if __name__ == '__main__':
#
#     parent_conn,child_conn = Pipe()   #双向管道
#     print('Q_ID2',id(child_conn))
#     p = Process(target=f,args=(child_conn,))
#     p.start()
#     print('儿子说：',parent_conn.recv())
#     parent_conn.send('乖儿子')
#     p.join()
'''
Managers
'''
from multiprocessing import Process,Manager

def f(d,l,n):
    d[n] = '1'
    d['2'] = 2

    l.append(n)

    print('Son process:',id(d),id(l))

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(5))
        print('Main process:',id(d),id(l))
        p_list = []

        for i in range(10):
            p = Process(target=f,args=(d,l,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)






