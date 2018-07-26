'''
class Hand:
    pass

class Foot:
    pass

class Head:
    pass

class Trunk:
    pass



class Preson:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.hand = Hand()
        self.foot = Foot()
        self.trunk = Trunk()
        self.head = Head()

p1 = Preson('2015','lxs')

print(p1.__dict__)


class School:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

        def zhaosheng(self):
           print('%s 正在招生' %self.name)

class Course:
    def __init__(self,name,price,period,school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school

s1 = School('lv','沾化')
s2 = School('lv','化1')
s3 = School('lv','沾2')

c1 = Course('linux',10000,'20d',s1)

print(c1.__dict__)
print(c1.school)
print(s1)
'''


class Hand:
    pass

class Foot:
    pass

class Head:
    pass

class Trunk:
    pass



class Preson:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.hand = Hand()
        self.foot = Foot()
        self.trunk = Trunk()
        self.head = Head()

p1 = Preson('2015','lxs')

#print(p1.__dict__)


class School:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

        def zhaosheng(self):

           print('%s 正在招生' %self.name)

class Course:
    def __init__(self,name,price,period,school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school

class Teacher:
    def __init__(self):
        pass




s1 = School('lv','沾化')
s2 = School('lv1','化1')
s3 = School('lv2','沾2')

c1 = Course('linux',10000,'20d',s1)

msg = '''
1 lv xxx
2 lv zzz
3 lv ccc
'''

menu = {
    '1':s1,
    '2':s2,
    '3':s3
}

choice = input('选择学校>>>: ')
school_obj = menu[choice]

name = input ('选择课程>>: ')
price = input ('课程费用>>: ')
period = input ('课程周期>>: ')

new_course = Course(name,price,period,school_obj)
print('课程【%s】属于【%s】学校' %(new_course.name,new_course.school.name))

