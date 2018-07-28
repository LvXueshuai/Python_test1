


# class P1:
#     pass
# class P2:
#     pass
#
# class P3(P1):  #单继承
#     pass
#
# class P4(P1,P2):  #多继承
#     pass

# class Dad:
#     money = 10000
#     def __init__(self,name):
#         print("爸爸")
#         self.name = name
#
#     def hit(self):
#         print('%s正在打儿子'%self.name)
#
# class Son(Dad):
#     money = 1000000000000000
#
# print(Dad.money)
# print(Son.money)
#
# print(Dad.__dict__)
# print(Son.__dict__)
#
# s1 = Son('llal')
# print(s1.name)
# print(s1.__dict__)
# s1.hit()



class Dad:
    money = 10000
    def __init__(self,name):
        print("爸爸")
        self.name = name

    def hit(self):
        print('%s正在打儿子'%self.name)

class Son(Dad):
    money = 1000000000000000

    def __init__(self,name,age):   #方法改写后以自己的为准
        self.name = name
        self.age = age
        print('%s的年龄为%s' %(self.name,self.age))
    def hit(self):
        print("来自儿子")

#s1 = Son('llal')    #缺少参数
s1 = Son('lv',22)
s1.hit()