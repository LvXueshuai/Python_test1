def Typed(**kwards):
    def deco(obj):
        print('====>', kwards)
        print('类名----------》', obj)
        for key,val in kwards.items():
            setattr(obj,key,val)
        # obj.x = 1
        # obj.y = 2
        # obj.z = 3
        return obj
    print('---->',kwards)
    return deco


@Typed(x=1,y=2,z=3)  #Typed(x=1,y=2,z=3) ---->deco  --->  @deco -->Foo=deco(Foo)
class Foo:
    print('我是Foo')


@Typed(name='lxs')
class Bar:
    pass
print(Bar.name)
