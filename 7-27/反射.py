class BlackMedium:
    feture = 'Ugly'
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

    def sell(self):
        print('【%s】正在卖房子' %self.name)

    def rent(self):
        print('【%s】正在租房子' %self.name)

b1 = BlackMedium('大哈比','山师')

b1.sell()
b1.rent()

print(hasattr(b1,'addr'))
print(hasattr(b1,'sell'))

print(getattr(b1,'name'))
print(getattr(b1,'rent'))
func = getattr(b1,'rent')
func()
print(getattr(b1,'rentsd','没找到啊！！！')) #找不到则显示最后的参数，如未给参数就报错


#setattr(x,y,v)  x为对象，y为要设置的key，v为value

setattr(b1,'daf','lala')
setattr(b1,'daf','lla')
print(b1.__dict__)

setattr(b1,'dad','lfrala')
print(b1.__dict__)
del b1.dad
print(b1.__dict__)

setattr(b1,'cnm','cnimlgb')
print(b1.__dict__)
#delattr(x,y)  y必须为字符串格式
delattr(b1,'cnm')
print(b1.__dict__)