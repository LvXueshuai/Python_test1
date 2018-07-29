# class Foo:
#     def __init__(self,x):
#         self.x = x
#
#
#     def __getattr__(self, item):
#         print('GETATTR')
#
#     def __getattribute__(self, item):  #属性有或者没有都会触发，即最先被触发
#         print('getattribute')
#
# f1 = Foo(10)
# f1.x

#
# print('------------------------------------------------>>>>>>>')
#
#
#
class Foo2:
    def __init__(self,x):
        self.x = x


    def __getattr__(self, item):
        print('GETATTR')

    def __getattribute__(self, item):  #属性有或者没有都会触发，即最先被触发
        print('getattribute')
        raise AttributeError('ERROR')

f2 = Foo2(10)
f2.x

