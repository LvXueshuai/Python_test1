l = list('hello')
print(l)

file = open('test.txt','w')
print(file)


class Foo:
   pass

f1 = Foo()
print(f1)   #---str(f1) --->f1.__str__()

print('------------------>')

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '%s的年龄是%s' %(self.name,self.age)

f1 = Foo('lxs',23)
print(f1)   #---str(f1) --->f1.__str__()

x = str(f1)
print(x)

y = f1.__str__()
print(y)


print('--------------------------------->>>>>>>>>>>>>>>>>')


class Foo2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):  #应用在解释器
        return '%s的年龄是%s' %(self.name,self.age)

f2 = Foo2('lxs',23)
print(f2)  #repr(f1) ----------->f1.__repr__()

# __str__()  __repr__()同时存在时先找str，即str不存在时再找repr


