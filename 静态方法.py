class Room:
    tag = 1
    def __init__(self,name,owner,width,length,hight):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.hight = hight

    @property   #封装    与实例绑定
    def cal_area(self):
        print('%s住的%s面积为%s' % ( r1.owner, r1.name,r1.width * r1.length))

    @classmethod    #类方法   与类绑定  自动传递类名     类级别的操作，与实例无关，但是实例也可以调用此函数
    def tell(cls):    #cls表示接受的应该为类名，与self作用类似
        print('--->tag = ',cls.tag)


    @staticmethod    #静态方法   类的工具包，不能使用类变量和实例变量
    def wash(a,b,c):
        print('%s %s %s正在洗澡' %(a,b,c))

    def tes(x,y):
        print(x,y)

Room.wash(1,2,3)

Room.tes(1,2)

r1 = Room("厕所",'lxs',100,25,60)
r1.wash(1,2,3)


print(Room.__dict__)
print(r1.__dict__)
