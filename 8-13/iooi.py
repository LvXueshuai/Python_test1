'''
事件驱动编程是一种编程范式，这里程序的执行由外部事件来决定，
他的特点是包含一个事件循环，当外部事件发生时使用回调机制来触发相应的处理
另外两种常见的编程范式是（单线程）同步以及多线程编程

'''


import gevent
import requests,time

start = time.time()

def f(url):
    print('GET: %s' %url)
    resp = requests.get(url)
    data = resp.text

    # f = open('new','w',encoding='utf8')
    # f.write(data)

    print('%d bytes received from %s' %(len(data),url))

f('https://www.baidu.com/')
f('https://www.yahoo.com/')
f('https://www.sina.com/')
# gevent.joinall([
#     gevent.spawn(f, 'https://www.baidu.com/'),
#     gevent.spawn(f, 'https://www.yahoo.com/'),
#     gevent.spawn(f, 'https://www.sina.com/'),
# ])


print('cost time:',time.time()-start)