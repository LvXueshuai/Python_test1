#
# print('===================')
# assert 1 == 2
# assert 1 == 1
#
#
# print('-------------------')

def test1():
    '逻辑1'
    res = 1
    return res

def test2():
    '逻辑2'
    res = 2
    return res


res1 = test1()
res2 = test2()

if res1 != 1:
    raise AssertionError
#两种方式结果相同
assert res1 == 1   #判断是否是想要的值


