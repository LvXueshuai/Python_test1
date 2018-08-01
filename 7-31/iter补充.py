# l = ['a','b','c','d']
#
# def test():
#     return l.pop()
#
# x = iter(test,'b')  #无限执行test（），直到运行结果为'b'
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())  #StopIteration

from functools import partial
def add(x,y):
    return x+y

func = partial(add,1)   #把1传给add函数的第一个值

print(func(1))
print(func(2))
print(func(5))











