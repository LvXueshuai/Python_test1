# isinstance(obj,cls)检查obj是否是类cls的对象
# issubclass(sub,super)检查sub类是否是super类的派生类

class Foo:
    pass

f1 = Foo()
print(isinstance(f1,Foo))  #检查f1是否是类Foo的对象


class Bar(Foo):
    pass

print(issubclass(Bar,Foo))  #检查Bar是否是Foo的子类



