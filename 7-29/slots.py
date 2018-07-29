#由__slots__ 类产生的实例不在具有__dict__属性   ，不可以再给实例添加新的属性即限制创建，只能应用已经创建的属性，不能创建新的

class Foo:
    __slots__ = ['name','age']   #{'name':None,'age':None}
    # __slots__= 'name '    #      {'name'}:None

f1 = Foo()
f1.name = 'lxs'   #__slots__


# f1.hgge = 18 #   -->steattr ------>f1.__dict['age'] = 18

print(f1.__slots__)

print('---------------------------------------------------->')
f2 = Foo()
f2.name = 'dsb'
f2.age = 22
print(f2.name)
print(f2.age)

print('------------------------------------------------------>')









