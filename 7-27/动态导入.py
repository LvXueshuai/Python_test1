# from m import t
# t.test1()
# from m.t import *
# test1()
# _test2()

moudle_t = __import__('m.t')   #返回最顶层模块 m
print(moudle_t)
#moudle_t.test1()
moudle_t.t.test1()

import importlib
m = importlib.import_module('m.t')
print(m)
m._test2()