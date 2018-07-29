# class Foo:
#     pass
#
# # l = list('hello')
# # for i in l:
# #     print(i)
#
# f1 = Foo()
# for i in f1:   #TypeError: 'Foo' object is not iterable
#     print(i)



class Foo:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 10000:
            raise StopIteration('STOP!!!')
        self.n += 1
        return self.n



f1 = Foo(10)
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())
print(next(f1))
print(next(f1))
print(next(f1))


for i in f1:  #f1.__iter__() == iter(f1)
    print(i)

