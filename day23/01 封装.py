'''
1、什么封装
    封：属性对外是隐藏的，但对内是开放的
    装：申请一个名称空间，往里装入一系列名字/属性

2、为什么要封装
    封装数据属性的目的
        首先定义属性的目的就是为了给类外部的使用者使用的，
        隐藏之后是为了不让外部使用直接使用，需要类内部开辟一个接口
        然后让类外部的使用通过接口来间接地操作隐藏的属性。
        精髓在于：我们可以在接口之上附加任意逻辑，从而严格控制使用者对属性的操作

    封装函数属性
        首先定义属性的目的就是为了给类外部的使用者使用的，
        隐藏函数属性是为了不让外部直接使用，需要类内部开辟一个接口
        然后在接口内去调用隐藏的功能
        精髓在于：隔离了复杂度



3、如何封装

'''
# 如何隐藏:在属性前加上__开头


#1、 这种隐藏仅仅只是一种语法上的变形操作
#2、 这种语法上的变形只在类定义阶段发生一次，因为类体代码仅仅只在类定义阶段检测一次
#3、 这种隐藏是对外不对内的，即在类的内部可以直接访问，而在类的外则无法直接访问，原因是
#    在类定义阶段，类体内代码统一发生了一次变形

#4、 如果不想让子类的方法覆盖父类的，可以将该方法名前加一个__开头


# class People:
#     __country='China' #_People__country='China'
#     __n=100 #_People__n=100
#     def __init__(self,name,age,sex):
#         self.__name=name #self._People__name=name
#         self.age=age
#         self.sex=sex
#
#     def eat(self):
#         print('eat.....')
#         print(People.__country) #People._People__country
#         print(self.__name) #self._People__name

# People.eat(123)
# print(People.__country)

# peo1=People('egon',18,'male')
# peo1.eat()
# print(peo1.__name)

# print(People.__dict__)
# print(People.__country)
# print(People._People__country)

# People.__x=11
# print(People.__dict__)


# peo1=People('egon',18,'male')
# print(peo1.__dict__)
# peo1.__x=111
# print(peo1.__dict__)

# class Foo:
#     def __f1(self): #_Foo__f1
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.__f1() #self._Foo__f1
#
# class Bar(Foo):
#     def __f1(self): #_Bar__f1
#         print('Bar.f1')
#
# obj=Bar()
# obj.f2()




class People:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def tell_info(self):
        print('%s:%s' %(self.__name,self.__age))

    def set_info(self,name,age):
        if type(name) is not str:
            # print('用户名必须为str类型')
            # return
            raise TypeError('用户名必须为str类型')

        if type(age) is not int:
            # print('年龄必须为int类型')
            # return
            raise TypeError('年龄必须为int类型')
        self.__name=name
        self.__age=age

peo1=People('egon',18)
# peo1.name=123
# peo1.age
# peo1.tell_info()

peo1.set_info('egon',19)
# peo1.tell_info()



