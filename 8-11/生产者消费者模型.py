import time,random
import queue,threading

q = queue.Queue()

def Producer(name):
    count = 1
    while count < 11:
        print('Making..........')
        time.sleep(random.randrange(3))   #产生随机数[1,3)即：1或2
        q.put(count)
        print('Producer %s has produced %s BaoZo...' %(name,count))
        count += 1
        #q.task_done()
        q.join()
        print('Ok!')

def Consumer(name):
    count = 1
    while count < 11:


        data = q.get()
        print('EATING')
        time.sleep(random.randrange(4))
        q.task_done()
        #q.join()
            # print(data)
        print('\033[32;1mConsumer %s has eat %s BaoZi...\033[0m' %(name,data))

        count += 1

p1 = threading.Thread(target=Producer,args=('A',))
c1 = threading.Thread(target=Consumer,args=('B',))
c2 = threading.Thread(target=Consumer,args=('C',))
c3 = threading.Thread(target=Consumer,args=('D',))

p1.start()
c1.start()
c2.start()
c3.start()