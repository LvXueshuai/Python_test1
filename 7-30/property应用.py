class People:
    def __init__(self,name):
        self.name = name   #实例化触发property

    @property
    def name(self):
        print('---GET---')
        return self.DOUNIWAN

    @name.setter
    def name(self,value):
        print('---SET---')
        if not isinstance(value,str):
            raise TypeError('必须是字符串类型')
        self.DOUNIWAN = value

    @name.deleter
    def name(self):
        print('---delete---')
        del self.DOUNIWAN

p1 = People('dsb')
print(p1.name)