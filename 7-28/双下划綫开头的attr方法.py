#双下划綫开头为内置
class Foo:
    x= 1
    def __init__(self,y):
        self.y = y

    def __getattr__(self, item):   #调用不存在的属性方法时被处罚
        print('执行__getattr__')

f1 = Foo(10)
print(f1.y)
print(getattr(f1,'y'))   #类似于  len(str) ---->str__len__()

f1.sssss   #触发__getattr__


print('------------------------------->')

class Foo:
    x= 1
    def __init__(self,y):
        self.y = y

    def __delattr__(self, item):   #删除一个对象的属性时被触发
        print('执行__delattr__')
        # del self.item   #无限递归
        # self.__dict__.pop(item) #应用这种方式

f1 = Foo(10)
del f1.y    #触发__delattr__
del f1.y



print('------------------------------->')
class Foo:
    x= 1
    def __init__(self,y):
        self.y = y  #触发__setattr__

    def __setattr__(self, key,value):   #设置值时被触发
        print('执行__setattr__')
        #self.key = value   #触发__setattr__无线递归死循环
        self.__dict__[key] = value


f1 = Foo(10)
print(f1.__dict__)
f1.z = 2
print(f1.__dict__)


print('------------------------------->')
print(dir(Foo))

print('------------------------------->')

class Foo:
    def __init__(self,name):
        self.name = name

    def __getattr__(self, item):
        print('找的属性【%s】不存在' %item)

    def __setattr__(self, key,value):
        print('执行__setattr__',key,value)
        if type(value) is str:
            print("开始设置")
            self.__dict__[key] = value
        else:
            print('必须为str类型')

    def __delattr__(self, item):
        print('执行__delattr__',item)
        self.__dict__.pop(item)

f1 = Foo('lala')
print(f1.name)
print(f1.age)  #属性不存在，触发__getattr__
print('------------------------------->')
f1.asd =18
f1.sgrjh = 'gkwenbo'

print(f1.__dict__)
print('------------------------------->')

del f1.sgrjh
print(f1.__dict__)

