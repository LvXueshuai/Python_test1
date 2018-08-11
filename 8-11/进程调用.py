# from multiprocessing import Process
# import time
#
# def f(name):
#     time.sleep(1)
#     print('Hello %s'%name,time.ctime())
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):
#         p = Process(target=f,args=('lxs',))  #多个进程
#         p_list.append(p)
#         p.start()
#     for i in p_list:
#         p.join()
#     print('END!')


# from multiprocessing import Process
# import time
#
# class MyP(Process):
#     def __init__(self):
#         super(MyP,self).__init__()
#
#     def run(self):
#         time.sleep(1)
#         print('Hello %s' % self.name, time.ctime())
#         '''
#         self.name 为进程名称  MyP-1\2\3 即类名加序号
#         '''
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):
#         p = MyP()  #多个进程
#         p.daemon = True   #守护进程
#         p.start()
#         p_list.append(p)
#
#     for i in p_list:
#         p.join()
#     print('END!')


import multiprocessing
import os
import time


def info(title):
    print('title:',title)
    print('parent process:',os.getppid())  #父进程
    print('process id:',os.getpid()) #本身进程

def f(name):
    info('function f')
    print('hello',name)

if __name__ == '__main__':
    info('main process line')
    time.sleep(1)


    '''
    title: main process line
    parent process: 12912
    process id: 18276
    '''
    print('-------------------------------')
    p = multiprocessing.Process(target=info,args=('lxs',))
    p.start()
    p.join()








