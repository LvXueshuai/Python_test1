'''
 列表是不安全的数据结构
 队    列是一种数据结构
 import queue   #  先进先出模式  线程队列
 q = queue.LifoQueue()   #先进后出模式
 q = queue.Queue(3)  #参数为可容纳数据
 q = queue.PriorityQueue()   #优先级
 q.put_nowait(x)相当于-->
 q.put(1,False)  #False表示若存满则报错不卡住    queue.Full
 q.task_done()在完成一项工作后，q.task_done()函数向任务已完成的队列发送一个信号
 q.join（）实际上意味着等到队列为空，在执行别的操作


 '''
#
# import threading,time
#
# li = [1,2,3,4,5]
#
# def pri():
#     while li:
#         a = li[-1]
#         print(a)
#         time.sleep(0.5)
#         try:
#             li.remove(a)
#         except Exception as e:
#             print('-------->',a,e)
#
# t1 = threading.Thread(target=pri,args=())
# t1.start()
# t2 = threading.Thread(target=pri,args=())
# t2.start()
#
'''
先进先出模式
'''
# import queue   #  先进先出模式  线程队列
#
#
# q = queue.Queue(3)  #参数为可容纳数据
#
# q.put(12)
# q.put('hello')
# q.put({'name':'lxs'})
#
# q.put(1,False)  #False表示若存满则报错不卡住    queue.Full
#
# while 1:
#     data = q.get()
#     print(data)
#     print('-------------====---------------')

# '''
# 先进后出模式
# '''
# import queue

# q = queue.LifoQueue()   #先进后出模式
#
# q.put(12)
# q.put('hello')
# q.put({'name':'lxs'})
#
# #q.put(1,False)  #False表示若存满则报错不卡住    queue.Full
#
# while 1:
#     data = q.get()
#     print(data)
#     print('-------------====---------------')

# import queue
#
# q = queue.PriorityQueue()   #优先级
#
# q.put([1,3])  #优先级为1
# q.put([4,'hello']) #优先级为4
# q.put([2,{'name':'lxs'}])  #优先级为2
#
# #q.put(1,False)  #False表示若存满则报错不卡住    queue.Full
#
# while 1:
#     data = q.get()
#     print(data)  #打印所有，包括优先级
#     print(data[1]) #打印内容
#     print('-------------====---------------')


import queue
q = queue.Queue(3)
q.put(12)
q.put('hello')
q.put({'name':'lxs'})


print(q.qsize())
print(q.empty())
print(q.full())










