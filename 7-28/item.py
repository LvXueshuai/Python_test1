class Foo:
    def __getitem__(self, item):
        print("getitem")
        return self.__dict__

    def __setitem__(self, key, value):  #dict fangshi
        print('setitem')
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('delitem')
        self.__dict__.pop(key)

f1 = Foo()
print(f1.__dict__)
f1['name'] = 'lxs'
f1['age'] = '23'
print(f1.__dict__)
print('-----------------------------------')
del f1.age

print(f1.__dict__)
print('-----------------------------------')
f1['name']
del f1['name']    #zidianfangshi diaoyong item
print(f1.__dict__)

