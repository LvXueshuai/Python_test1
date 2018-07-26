def dog(name,gender,type):
    def jiao(dog):
        print('一条狗%s汪汪汪'%dog['name'])
    def chi(dog):
        print('一条%s的%s的正在吃屎'% (dog['gender'],dog['type']))
    def inie(name,gender,type):
        dog1 = {
            'name':name,
            'gender':gender,
            'type':type,
            'jiao':jiao,
            'chi':chi,
        }
        return dog1
    res = inie(name,gender,type)
    return res
d1 = dog('sb','man','ss')
print(d1)

d1['jiao'](d1)
d1['chi'](d1)