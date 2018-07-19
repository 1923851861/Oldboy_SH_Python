'''
1、什么是继承
    继承是一种新建类的方式，新建的类称为子类，被继承的类称为父类
    继承的特性是：子类会遗传父类的属性
    强调：继承是类与类之间的关系

2、为什么用继承
    继承的好处就是可以减少代码的冗余

3、如何用继承
    在python中支持一个类同时继承多个父类
    在python3中
        如果一个类没有继承任何类，那默认继承object类
    在python2中：
        如果一个类没有继承任何类，不会继承object类

    新式类
        但凡继承了object的类以及该类的子类，都是新式类
    经典类
        没有继承object的类以及该类的子类，都是经典类

    在python3中都是新式类，只有在python2中才区别新式类与经典类

    新式类vs经典类?

'''
class Parent1(object):
    pass

class Parent2(object):
    pass

class Sub1(Parent1,Parent2):
    pass

print(Sub1.__bases__)
# print(Parent1.__bases__)
# print(Parent2.__bases__)