'''
gerrnlet是一个 用C实现的协程模块，相比于python自带的yield模块，
    可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator


'''

from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()  #进行切换
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()   #执行
