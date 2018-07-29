# class Foo:
#     pass
#
# f1 = Foo()
#
# f1()   #TypeError: 'Foo' object is not callable


print('-----------------------------------------------')

class Foo:
    print('lalaal')
    def __call__(self, *args, **kwargs):
        print("Start")

f1 = Foo()

f1()

print('--------------------')
Foo()