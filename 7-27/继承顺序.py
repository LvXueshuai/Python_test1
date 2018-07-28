#python可以继承多个类  寻找方法：深度优先和广度优先
#python 3.X 都是新式类，使用广度优先，不会找基类（本例中的A）    本例：F -> D -> B -> E -> C ->A
class A:
    def test(self):
        print('A')

class B(A):
    pass
    # def test(self):
    #     print('B')

class C(A):
    def test(self):
        print('C')

class D(B):
    pass

    # def test(self):
    #     print('D')

class E(C):
    def test(self):
        print('E')

class F(D,E):
    # def test(self):
    #     print('F')
    pass

f1 = F()
f1.test()

print(F.__mro__)
#MRO列表就是一个简单的所有基类的线性顺序列表    C3线性化算法实现
#1.子类优先父类被检查
#2.若多个父类，会根据其在列表的顺序被检查
#3.若对下一个类存在两个合法的选择，选择第一个父类
