'''
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，
    如果进程池中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止
进程池中有两个方法：
    apply
    apply_async

'''


from multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(1)
    print(i)
    return i+100
'''
Bar 函数的参数arg为Foo函数的返回值(i+100)
'''
def Bar(arg):

    print(os.getpid())
    print(os.getppid())
    print('Logger:',arg)



if __name__ == '__main__':
    pool = Pool()
    '''#进程池对象，最大进程数为5
        如果不写参数，则默认为cpu核心数
    '''

    # Bar(1)
    # print('-------------------------')

    for i in range(40):
        # pool.apply(func = Foo,rgs=(i,)) #同步接口，一个一个走，与进程池无关
        # pool.apply_async(func=Foo, args=(i,))
        pool.apply_async(func=Foo,args=(i,),callback=Bar)
        '''回调函数： claaback属于主进程调用
            某个动作或者函数执行成功后再去执行的函数
            回调函数的参数为子进程的返回值
        '''


    pool.close()
    '''
    进程池里close必须在join之前，不可更改
    
    '''
    pool.join()
    print('END')