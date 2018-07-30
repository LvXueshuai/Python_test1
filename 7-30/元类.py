# class Foo:
#     pass
#
# f1 = Foo()
#
# print(type(f1))
# print(type(Foo))   #产生类的类就是type

'''
元类是类的类，是类的模板
元类是用来控制如何创建类的，正如类是创建对象的模板
元类的实例是类，类的实例是对象
type是python的一个内建类，用来直接控制生成类，python中任何class定义的类其实都是type类实例化的对象
'''

class Foo:
    def __init__(self):
        pass
print(Foo)
print(Foo.__dict__)


def __init__(self,name,age):
    self.name = name
    self.age = age

def test(self):
    print('----TEST---')

FFo = type('FFo',(object,),{'x':1,'__init__':__init__,'test':test})   #类由元类创建而来
print(FFo)
print(FFo.__dict__)

f1 = FFo('DSB',18)
print(f1.name)
f1.test()




