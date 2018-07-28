

import test as obj

print(obj)

print(hasattr(obj,'say'))

if hasattr(obj,'say'):
    func = getattr(obj,'say')
    func()
else:
    print('no！！！！！！！')

print('------------------------------------->')

x = 111111

# import fanshe as a  #导入过程会执行一次
# print('-->',hasattr(a,'x'))

import sys
obj1 = sys.modules[__name__]
print('-->',hasattr(obj1,'x'))       #一切皆对象，反射可用于各处



