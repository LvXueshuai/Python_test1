#析构函数的调用室友解释器再进行垃圾回收是自动触发执行的

class Foo:
    def __init__(self,name):
        self.name = name

    def __del__(self):  #实例被删除是执行
        print('Start')

f1 = Foo('lxs')
del f1.name  #只是删除实例的属性，不会执行__del__
# print('****************')  #执行完之后自动释放进行垃圾回收，执行__del__
print('>>>>>>>>>>>>>>>>>>>>>>>>')
del f1   #实例被删除，执行__del__
print('------------------->')


