import threading,time

class Boss(threading.Thread):
    def run(self):
        print('BOSS**************>')
        print(event.isSet())
        event.set()
        time.sleep(2)
        print('Boss : Fuck@!!!')
        print(event.isSet())
        event.set()


class Worker(threading.Thread):
    def run(self):

        event.wait()  #一旦EVEN被设定，视为pass
        print('Worker: 八嘎')
        time.sleep(1)
        event.clear() #清除set
        event.wait()
        print('Worker : 吆西')

if __name__ == '__main__':
    event = threading.Event()

    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('ENDING!!!!!')