class Lazyproperty:
    # print('-------->LAZY')
    def __init__(self,func):
        print('----------->FUNC')
        self.func = func
    def __get__(self, instance, owner):
        print('GET')

        if instance is None:
            return self
        res = self.func(instance)
        setattr(instance,self.func.__name__,res) #存入字典
        return res


class Room:

    def __init__(self,name,width,length):
        self.name = name
        self.width = width
        self.length = length

    # @property    #area = property(area)
    @Lazyproperty   #area = Lazyproperty(area)   给类增加描述符
    def area(self):
        return self.width * self.length

    @property
    def area1(self):
        return self.width * self.length

    @property
    def test(self):
        return '@property'

# r1 = Room('dsb',5,10)
# print(r1.area)
# print(Room.__dict__)  # 'area': <property object at 0x0000000000611BD8>,

#实例调用
r1=Room('cnm',6,7)
print(r1.area)
print(r1.__dict__)
print(r1.area)  #从实例字典里调用，不再触发__get__方法，已经存在字典里
print(r1.area)






# print(r1.area1)

#类调用
# print(Room.area)
#
# print(r1.test)
# print(Room.test)






