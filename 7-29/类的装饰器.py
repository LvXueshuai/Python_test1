#一切皆对象
# def d(func):
#     print('----------')
#     return func
#
# @d   #test = d(test)
# def test():
#     print('test运行')
#
# test()
#
#
#
# @d   #Foo=d(Foo)
# class Foo:
#     pass
#
# f1 = Foo




def deco(obj):
    print('----------',obj)
    obj.x = 1
    obj.y = 2
    obj.z = 3
    return obj

@deco   #Foo=deco(Foo)
class Foo:
    pass

print(Foo.__dict__)

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

# @deco
# def test():
#     print('TEST')

