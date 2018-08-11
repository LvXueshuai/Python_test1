# import threading
# import time
#
#
# def music():
#     print('Begin listen %s' %time.ctime())
#     time.sleep(3)
#     print('Stop listen %s' %time.ctime())
#
# def game():
#     print('Begin play %s' % time.ctime())
#     time.sleep(5)
#     print('Stop play %s' % time.ctime())
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=music)
#     t2 = threading.Thread(target=game)
#
#     t1.start()
#     t1.join()  # 在子线程完成运行之前，子线程的父县城将一直被阻塞
#     t2.start()
#
#     # t1.join() #在子线程完成运行之前，子线程的父线程将一直被阻塞
#     t2.join()
#
#     print('ENDING')
#
#
#
#
#
#     # print('ENDING!') #主线程
#
#
#
# import threading
# import time
#
#
# def music():
#     print('Begin listen %s' %time.ctime())
#     time.sleep(3)
#     print('Stop listen %s' %time.ctime())
#
# def game():
#     print('Begin play %s' % time.ctime())
#     time.sleep(5)
#     print('Stop play %s' % time.ctime())
#
#
# threads = []
# t1 = threading.Thread(target=music)
# t2 = threading.Thread(target=game)
#
# threads.append(t1)
# threads.append(t2)
#
#
# if __name__ == '__main__':
#     t2.setDaemon(True)  # 守护线程,一定在start之前，随着主线程退出而退出，不管自己是否完成。
#     for t in threads:
#         t.start()
#     print('ENDING')

import threading
import time


def music():
    print('Begin listen %s' %time.ctime())
    time.sleep(1)
    print('Stop listen %s' %time.ctime())

def game():
    print('Begin play %s' % time.ctime())
    time.sleep(2)
    print('Stop play %s' % time.ctime())


threads = []
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=game)

threads.append(t1)
threads.append(t2)


if __name__ == '__main__':
    #t2.setDaemon(True)  # 守护线程,一定在start之前，随着主线程退出而退出，不管自己是否完成。
    for t in threads:
        t.start()
        print(t.getName())  #获取线层名称
        print(threading.currentThread())
        print(threading.current_thread())
        print('COUNT:',threading.active_count())

    print('ENDING!') #主线程







