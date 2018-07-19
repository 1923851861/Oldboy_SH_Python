#派生：子类中新定义的属性，子类在使用时始终以自己的为准
class OldboyPeople:
    school = 'oldboy'
    def __init__(self,name,age,sex):
        self.name = name #tea1.name='egon'
        self.age = age #tea1.age=18
        self.sex = sex #tea1.sex='male'

class OldboyStudent(OldboyPeople):
    def choose_course(self):
        print('%s is choosing course' %self.name)

class OldboyTeacher(OldboyPeople):
    #            tea1,'egon',18,'male',10
    def __init__(self,name,age,sex,level):
        # self.name=name
        # self.age=age
        # self.sex=sex
        OldboyPeople.__init__(self,name,age,sex)
        self.level=level

    def score(self,stu_obj,num):
        print('%s is scoring' %self.name)
        stu_obj.score=num

stu1=OldboyStudent('耗哥',18,'male')
tea1=OldboyTeacher('egon',18,'male',10)
# print(stu1.__str__())
# print(tea1.__dict__)

#对象查找属性的顺序：对象自己-》对象的类-》父类-》父类。。。
# print(stu1.school)
# print(tea1.school)
# print(stu1.__dict__)
# print(tea1.__dict__)

# tea1.score(stu1,99)

# print(stu1.__dict__)


# 在子类派生出的新功能中重用父类功能的方式有两种：
#1、指名道姓访问某一个类的函数：该方式与继承无关


# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')

# #对象查找属性的顺序：对象自己-》对象的类-》父类-》父类。。。
# obj=Bar()
# obj.f2()
# '''
# Foo.f2
# Bar.f1
# '''