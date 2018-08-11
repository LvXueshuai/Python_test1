# import threading
#
# def sub():
#     global num
#     num -= 1
#
# num = 100
#
# l = []
#
# for i in range(100):
#     t= threading.Thread(target=sub)
#     t.start()
#     l.append(t)
#
# for t in l:
#     t.join()
#
# print(num)


import threading
import time

def sub():
    global num

    lock.acquire()   #锁死下边内容，不允许切换
    temp = num
    time.sleep(0.001) #中间发生切换，导致结果出误差
    num = temp - 1
    lock.release()   #释放锁

num = 100

l = []
lock = threading.Lock()   #锁
for i in range(100):
    t= threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()

print(num)


