'''
进程线程：抢占式
协程：又称微线程，纤程，Coroutine   执行效率高
    主要解决IO操作
    协作式，非抢占
    关键词 -->  yield（）
    用户态的切换
    本质上就是一个线程，不能用多核
'''


import time
import queue

def consumer(name):    #生成器
    print('--->Ready')
    while True:
        new_baozi = yield
        print('【%s】 is eaing %s' %(name,new_baozi))
        time.sleep(1)

def producer():

    r = con.__next__()
    r = con2.__next__()

    n = 0
    while 1:
        time.sleep(1)
        print('Baozi %s and %s'%(n,n+1))
        con.send(n)
        con2.send(n+1)

        n += 2

if __name__ == '__main__':
    con = consumer('c1')
    con2 = consumer('c2')
    p = producer()







