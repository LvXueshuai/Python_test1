
class List(list):
    pass

l1 = List('hello world')
print(l1,type(l1))
#相当于
l2 = list('hello world')
print(l2,type(l2))

print('----------------------------------->')
class List(list):
    def show(self):
        mid = int(len(self)/2)
        return self[mid]

    def append(self,i):
        if type(i) is str:
            #self.append(self.item)   #溢出
            #list.append(self,i)  #可用
            super().append(i)
l1 = List('helloworld')
print(l1,type(l1))
#相当于
l2 = list('helloworld')
print(l2,type(l2))

print(l1.show())
l1.append('fgdjh')
print(l1,type(l1))