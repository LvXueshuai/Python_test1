
def test(x):
    print('-->',x)

test('sdg')
print('----------------------------------------------->')


class Typed:
    def __init__(self,key,expected_type):
        self.key = key
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        print('GET')
        # print('instance------>',instance)
        # print('owner-------->',owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value,):
        print('SET')
        #print('instance-------->', instance)
        # print('value----------->', value)
        # print('==================>SELF：',self)
        if not isinstance(value,self.expected_type):   #判断传入值是否符合规定
            # print('input Error')
            # return
            raise TypeError('%s传值错误' %self.expected_type)
        # print(self.key)
        instance.__dict__[self.key]= value

    def __delete__(self, instance):
        print('DELETE')
        # print('instance--------->', instance)
        instance.__dict__.pop(self.key)

class People:
    name = Typed('name', str, )
    age = Typed('age', int)
    salary = Typed('salary', float)
    def __init__(self,name,age,salary):
        self.name = name   #触发代理而bu 是实例
        self.age = age
        self.salary = salary


p1 = People('lala',22,500000.252)

print(p1.__dict__)
print(p1.age)

# print('==========================')
# p1.name = 'das'
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)



# p1.name = 'das'
# print(p1.__dict__)
# print(p1.name)

print('********************************************')
# p2 = People(33,22,500000.54)
# print(p2.__dict__)



