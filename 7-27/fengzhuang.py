
__author__ = '吕雪帅'

class People:
    _star = 'earth'  #单下划线开头表示被隐藏,仅仅是一种约定，不会阻止实例访问
    __star2 = 'hahaha'
    def __init__(self,id,name,age,salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def get_id(self):
        print('找到的ID为%s' %self.id)

print(People.__dict__)

p1 = People(55,'hg',22,38000)

print(p1._star)

print(People.__dict__)
print(p1._People__star2)
# import sys
# print(sys._home)