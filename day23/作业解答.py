# 1、定义MySQL类（参考答案：http://www.cnblogs.com/linhaifeng/articles/7341177.html#_label5）
#
# 　　1.1.对象有id、host、port三个属性
#
# 　　1.2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一
#
# 　　1.3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化
#
# 　　1.4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号，
#         保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象
#
import uuid
import settings
import pickle
import os
class MySQL:
        def __init__(self,host,port):
                self.id=self.create_id
                self.host=host
                self.host=port

        def save(self):
                pass


        @classmethod
        def from_conf(cls):
                return cls(settings.HOST,settings.PORT)

        @staticmethod
        def create_id():
                return str(uuid.uuid1())
obj1=MySQL.from_conf()


# 2、定义一个类：圆形，该类有半径，周长，面积等属性，将半径隐藏起来，将周长与面积开放
# 	参考答案（http://www.cnblogs.com/linhaifeng/articles/7340801.html#_label4）
#
#


# 3、明日默写
# 	1、简述面向对象三大特性：继承、封装、多态
# 解答：
#         继承：
#              继承是一种新建类的方式，新建的类称为子类，被继承的类称为父类
#              特性：子类会遗传父类的属性（强调：继承是类与类之间的关系）
#         封装：
#              封：属性对外是隐藏的，但对内是开放的
#              装：申请一个名称空间，往里装入一系列名字/属性
#              封装数据属性目的：
#                       在定义属性中隐藏其属性，将开辟接口让类外使用者
#                       通过接口访问其属性
#              精髓在于：我们可以在接口之上附加任意逻辑，从而严格控制使用者对属性的操作
#               封装函数属性目的：
#                       在定义属性中隐藏函数属性，将开辟一个接口调用隐藏功能
#               精髓在于：隔离复杂度
#         多态：
#              多态指的是同一种事物的多种形态（水---》冰、雪、水蒸汽）
#              多态性：继承同一类的多个子类中有相同的方法名
#              子类产生的对象就可以不用考虑具体的类型而直接调用功能
#               父类是指定标准的，不能被实例化
#               python推崇鸭子类型
#
#
#
# 	2、定义一个人的类，人有名字，身高，体重，用property将体质参数封装成人的数据属性
# class People:
#         def __init__(self,name,height,weight):
#                 self.name=name
#                 self.height=height
#                 self.weight=weight
#         @property
#         def bmi(self):
#                 return self.weight / (self.height ** 2)
# peo1=People('egon',1.8,75)
# print(peo1.bmi)


# 	3、简述什么是绑定方法与非绑定方法，他们各自的特点是什么？
# 、绑定方法
#     特性：绑定给谁就应该由谁来调用，谁来调用就会将谁当作第一个参数自动传入
#          《《《精髓在于自动传值》》》
#
#     绑定方法分为两类:
#         1.1 绑定给对象方法
#             没有装饰器修饰的情况下在类内部定义的函数，默认就是绑定给对象用的
#         1.2 绑定给类的方法：
#             在类内部定义的函数如果被装饰器@classmethod装饰，
#             那么则是绑定给类的，应该由类来调用，类来调用就自动将类当作第一个参数自动传入
#
# 2、非绑定方法
#     类中定义的函数如果被装饰器@staticmethod装饰，那么该函数就变成非绑定方法
#     既不与类绑定，又不与对象绑定，意味着类与对象都可以来调用
#     但是无论谁来调用，都没有任何自动传值的效果，就是一个普通函数
#

# 3 应用
#     如果函数体代码需要用外部传入的类，则应该将该函数定义成绑定给类的方法
#     如果函数体代码需要用外部传入的对象，则应该将该函数定义成绑定给对象的方法
#     如果函数体代码既不需要外部传入的类也不需要外部传入的对象，则应该将该函数定义成非绑定方法/普通函数


class MySQL:
    def __init__(self,host,port):
        self.id=self.create_id()
        self.host=host
        self.port=port

    def save(self):
        if not self.is_exists:#判断文件是否存在
            raise PermissionError('对象已存在')
        file_path=r'%s%s%s' %(settings.DB_PATH,os.sep,self.id)#定位到settings中DB_PATH指向的路径，以uuid计算得出的id命令的文件
        pickle.dump(self,open(file_path,'wb'))#序列化打开文件

    @property
    def is_exists(self):#定义文件
        tag=True
        files=os.listdir(settings.DB_PATH)#打开文件路径
        for file in files:
            file_abspath=r'%s%s%s' %(settings.DB_PATH,os.sep,file)#读取文件路径，系统路径分割符，文件
            obj=pickle.load(open(file_abspath,'rb'))#读取文件
            if self.host == obj.host and self.port == obj.port:#当传入的host和文件中的host以及传入的port以及文件中的商品相同时
                tag=False#存在即false
                break
        return tag

    @staticmethod
    def get_obj_by_id(id):#获取id
        file_abspath = r'%s%s%s' % (settings.DB_PATH, os.sep, id)#打开文件id
        return pickle.load(open(file_abspath,'rb'))#返回反序列化文件

    @staticmethod
    def create_id():#创建id
        return str(uuid.uuid1())#返回id

    @classmethod
    def from_conf(cls):#获取settings文件中的某些属性
        print(cls)
        return cls(settings.HOST,settings.PORT)#返回settigs文件中的HOST,PORT

# print(MySQL.from_conf) #<bound method MySQL.from_conf of <class '__main__.MySQL'>>
conn=MySQL.from_conf()
conn.save()

conn1=MySQL('127.0.0.1',3306)
conn1.save() #抛出异常PermissionError: 对象已存在


obj=MySQL.get_obj_by_id('7e6c5ec0-7e9f-11e7-9acc-408d5c2f84ca')
print(obj.host)