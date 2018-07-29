

print('----------------------------------------------->')


class Typed:
    def __init__(self,key,expected_type):
        self.key = key
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        print('GET')
        return instance.__dict__[self.key]

    def __set__(self, instance, value,):
        # print('SET')

        if not isinstance(value,self.expected_type):   #判断传入值是否符合规定
            raise TypeError('%s传值错误' %self.expected_type)
        instance.__dict__[self.key]= value

    def __delete__(self, instance):
        print('DELETE')
        instance.__dict__.pop(self.key)

def deco(**kwards):
    def wrapper(obj):
        # print('====>', kwards)
        # print('类名----------》', obj)
        for key,val in kwards.items():
            print('>>>>>>',key,val)
            setattr(obj,key,Typed(key,val))
            # setattr(obj,key,val)

        return obj
    # print('---->',kwards)
    return wrapper

@deco(name=str,age=int,salary=float,gender=str,hights=float)
    #@wrapper --->People=wrapper(People)
class People:
    # name = Typed('name', str, )
    # age = Typed('age', int)
    # salary = Typed('salary', float)
    # gender = Typed('salary', str)
    # hights = Typed('hights', float)
    def __init__(self,name,age,salary,gender,hights):
        self.name = name   #触发代理而bu 是实例
        self.age = age
        self.salary = salary
        self.gender = gender
        self.hights = hights


p1 = People('lala',22,500000.252,'nam',1.73)
print(p1.__dict__)
print(People.__dict__)



