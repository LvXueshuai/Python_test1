#接口继承   父类只定义接口，不定义具体实现

import abc    #让父类可以限制子类     归一化，一切皆文件
class All(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):       #接口类的方法不用具体实现，目的是规范子类
        pass

    @abc.abstractmethod
    def write(self):
        pass

class Disk(All):
    def read(self):
        print('disk read')
    def write(self):
        print('disk write')

class Cdrom(All):
    def read(self):
        print('cdrom read')
    def write(self):
        print('cdrom write')

class Men(All):
    def read(self):
        print('men read')
    def write(self):
        print('men write')
m1 = Men()




