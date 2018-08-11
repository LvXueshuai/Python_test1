import threading,time

class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(2)
            semaphore.release()


if __name__ == '__main__':
    semaphore = threading.Semaphore(5)   #信号量，最多同时有五个现程
    thrs = []

    for i in range(15):
        thrs.append(MyThread())
    for t in thrs:
        t.start()