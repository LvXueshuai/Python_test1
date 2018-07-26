class Room:
    tag = 1
    def __init__(self,name,owner,width,length,hight):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.hight = hight

    @property   #封装
    def cal_area(self):
        print('%s住的%s面积为%s' % ( r1.owner, r1.name,r1.width * r1.length))

    @classmethod    #类方法  自动传递类名     类级别的操作，与实例无关，但是实例也可以调用此函数
    def tell(cls):    #cls表示接受的应该为类名，与self作用类似
        print('--->tag = ',cls.tag)


r1 = Room("厕所",'lxs',100,25,60)
r1.cal_area

Room.tell()
#若前边没有@property  应该为r1.cal_area()

