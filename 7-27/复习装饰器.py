import time
#装饰器框架   装饰器 = 高阶函数 + 函数嵌套 + 闭包
def timer(func):
    def wrapper():
        #print(func)
        start = time.time()
        func()  #就是在运行test()
        end = time.time()
        print('Time =%s'%(end - start))
    return wrapper
@timer    # @timer 相当于test = timer(test)
def test():
    time.sleep(1)
    print("Start")
    print('End')

#test = timer(test)   #返回的是wrapper的地址
#test() #执行wrapper
test()
