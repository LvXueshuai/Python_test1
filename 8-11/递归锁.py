# import threading
# import time
#
# '''
# 产生死锁
# Thread-1 got A Sat Aug 11 15:27:31 2018
# Thread-1 got B Sat Aug 11 15:27:33 2018
# Thread-1 got B Sat Aug 11 15:27:34 2018Thread-2 got A Sat Aug 11 15:27:34 2018
# 线程1等待A锁，线程2等待B锁，
# '''
# class MyThread(threading.Thread):
#
#     def actionA(self):
#         A.acquire()
#         print(self.name,'got A',time.ctime())
#         time.sleep(2)
#
#         B.acquire()
#         print(self.name, 'got B', time.ctime())
#         time.sleep(1)
#
#         B.release()
#         A.release()
#
#     def actionB(self):
#         B.acquire()
#         print(self.name, 'got B', time.ctime())
#         time.sleep(2)
#
#         A.acquire()
#         print(self.name, 'got A', time.ctime())
#         time.sleep(1)
#
#         A.release()
#         B.release()
#
#     def run(self):
#         self.actionA()
#         self.actionB()
#
# if __name__ == '__main__':
#     A = threading.Lock()
#     B = threading.Lock()
#
#     L = []
#
#     for i in range(5):
#         t = MyThread()
#         t.start()
#         L.append(t)
#
#     for i in L:
#         i.join()
#
#     print('ENDING!')



import threading
import time

'''
RLOCK()递归锁
'''
class MyThread(threading.Thread):

    def actionA(self):
        r_lock.acquire()
        print(self.name,'got A',time.ctime())
        time.sleep(2)

        r_lock.acquire()
        print(self.name, 'got B', time.ctime())
        time.sleep(1)

        r_lock.release()
        r_lock.release()

    def actionB(self):
        r_lock.acquire()
        print(self.name, 'got B', time.ctime())
        time.sleep(2)

        r_lock.acquire()
        print(self.name, 'got A', time.ctime())
        time.sleep(1)

        r_lock.release()
        r_lock.release()

    def run(self):
        self.actionA()
        self.actionB()

if __name__ == '__main__':
    # A = threading.Lock()
    # B = threading.Lock()

    r_lock = threading.RLock()  #递归锁

    L = []

    for i in range(5):
        t = MyThread()
        t.start()
        L.append(t)

    for i in L:
        i.join()

    print('ENDING!')


