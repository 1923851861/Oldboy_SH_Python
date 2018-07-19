'''
1、绑定方法
    特性：绑定给谁就应该由谁来调用，谁来调用就会将谁当作第一个参数自动传入
         《《《精髓在于自动传值》》》

    绑定方法分为两类:
        1.1 绑定给对象方法
            在类内部定义的函数（没有被任何装饰器修饰的），默认就是绑定给对象用的
        1.2 绑定给类的方法：
            在类内部定义的函数如果被装饰器@classmethod装饰，
            那么则是绑定给类的，应该由类来调用，类来调用就自动将类当作第一个参数自动传入



2、非绑定方法
    类中定义的函数如果被装饰器@staticmethod装饰，那么该函数就变成非绑定方法
    既不与类绑定，又不与对象绑定，意味着类与对象都可以来调用
    但是无论谁来调用，都没有任何自动传值的效果，就是一个普通函数





3 应用
    如果函数体代码需要用外部传入的类，则应该将该函数定义成绑定给类的方法
    如果函数体代码需要用外部传入的对象，则应该将该函数定义成绑定给对象的方法
    如果函数体代码既不需要外部传入的类也不需要外部传入的对象，则应该将该函数定义成非绑定方法/普通函数



'''

# class Foo:
#     @classmethod
#     def f1(cls):
#         print(cls)
#
#     def f2(self):
#         print(self)
#
#
# obj=Foo()
# print(obj.f2)
# print(Foo.f1)

# Foo.f1()
# print(Foo)


#1、f1绑定给类的
# 了解：绑定给类的应该由类来调用，但对象其实也可以使用，只不过自动传入的仍然是类
# print(Foo.f1)
# print(obj.f1)
# Foo.f1()
# obj.f1()

#2、f2是绑定给对象的
# obj.f2()
# Foo.f2(obj)

import settings
import uuid

class Mysql:
    def __init__(self,ip,port):
        self.uid=self.create_uid()
        self.ip=ip
        self.port=port

    def tell_info(self):
        print('%s:%s' %(self.ip,self.port))

    @classmethod
    def from_conf(cls):
        return cls(settings.IP, settings.PORT)

    @staticmethod
    def func(x,y):
        print('不与任何人绑定')

    @staticmethod
    def create_uid():
        return uuid.uuid1()



# 默认的实例化方式：类名(..)
obj=Mysql('10.10.0.9',3307)

# 一种新的实例化方式：从配置文件中读取配置完成实例化
# obj1=Mysql.from_conf()
# obj1.tell_info()

# obj.func(1,2)
# Mysql.func(3,4)
# print(obj.func)
# print(Mysql.func)

print(obj.uid)