#__doc__属性无法被继承

#每个类都会默认有__doc__   不允许删除
class Foo:
    '我是__doc__描述信息'
    pass

class Bar(Foo):
    pass

# print(Bar.__doc__)   #该属性无法继承给子类

print(Foo.__dict__)
print(Bar.__dict__)


