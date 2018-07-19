#coding:utf-8
'''
1、菱形继承
    当一个子继承多个父类时，多个父类最终继承了同一个类，称之为菱形继承

2、菱形继承的问题：
    python2区分经典类与新式类，如果子的继承是一个菱形继承，那么经典类与形式的区别为？
        经典类下查找属性：深度优先查找
        新式类下查找属性：广度优先查找



'''

class G(object):
    # def test(self):
    #     print('from G')
    pass

class E(G):
    # def test(self):
    #     print('from E')
    pass

class B(E):
    # def test(self):
    #     print('from B')
    pass

class F(G):
    # def test(self):
    #     print('from F')
    pass

class C(F):
    # def test(self):
    #     print('from C')
    pass

class D(G):
    # def test(self):
    #     print('from D')
    pass

class A(B,C,D):
    def test(self):
        print('from A')
    # pass

obj=A()
print(A.mro())
# obj.test() #A->B->E-C-F-D->G-object