class MyType(type):
    def __init__(self,a,b,c):
        print('---元类的构造函数执行---')
        # print(a)
        # print(b)
        # print(c)

    def __call__(self, *args, **kwargs):
        print('=-=-=-=-=-=----->')
        #print(self)   #<class '__main__.Foo'>
        obj = object.__new__(self)  #object__new__(Foo)    --->产生f1
        self.__init__(obj,*args,**kwargs)  #Foo.__init__(f1,*arge,**kwargs)
        return obj


class Foo(metaclass=MyType):  #定义元类为MyType  即：   MyType('Foo'(object),{})
    def __init__(self,name):
        self.name = name

print(Foo)
f1 = Foo('name')
#print(f1.__dict__)  #'NoneType' object has no attribute '__dict__'
print(f1)



