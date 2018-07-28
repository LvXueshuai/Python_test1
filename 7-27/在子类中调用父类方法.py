'''
class Vehicle:
    country = 'China'
    def __init__(self,name,speed,load,power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power
    def run(self):
        print('%s开动了' %self.name)

class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        Vehicle.__init__(self,name,speed,load,power)
        self.line = line

    def show_info(self):
        print(self.name,self.speed,self.load,self.power,self.line )

    def run(self):
        Vehicle.run(self)
        print('%sDE%s开动了' %(self.name,self.line))




line13 = Subway('a','b',10000,'c',13)
line13.run()
line13.show_info()
'''

#super方法
class Vehicle:
    country = 'China'
    def __init__(self,name,speed,load,power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power
    def run(self):
        print('%s开动了' %self.name)

class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        #Vehicle.__init__(self,name,speed,load,power)
        super().__init__(name,speed,load,power,)
        self.line = line

    def show_info(self):
        print(self.name,self.speed,self.load,self.power,self.line )

    def run(self):
        #Vehicle.run(self)
        super().run()
        print('%sDE%s开动了' %(self.name,self.line))




line13 = Subway('a','b',10000,'c',13)
line13.run()
line13.show_info()