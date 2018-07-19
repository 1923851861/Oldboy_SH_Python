


# 在子派生的新方法中重用父类功能的两种方式
# 方式一：与继承无关
#指名道姓法，直接用：类名.函数名
# class OldboyPeople:
#     school = 'oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# class OldboyStudent(OldboyPeople):
#     def __init__(self,name,age,sex,stu_id):
#         OldboyPeople.__init__(self,name,age,sex)
#         self.stu_id=stu_id
#
#     def choose_course(self):
#         print('%s is choosing course' %self.name)


# 方式二：严格以来继承属性查找关系
# super()会得到一个特殊的对象，该对象就是专门用来访问父类中的属性的（按照继承的关系）
# super().__init__(不用为self传值)
# 注意：
# super的完整用法是super(自己的类名,self),在python2中需要写完整，而python3中可以简写为super()
# class OldboyPeople:
#     school = 'oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# class OldboyStudent(OldboyPeople):
#     def __init__(self,name,age,sex,stu_id):
#         # OldboyPeople.__init__(self,name,age,sex)
#         super(OldboyStudent,self).__init__(name,age,sex)
#         self.stu_id=stu_id
#
#     def choose_course(self):
#         print('%s is choosing course' %self.name)
#
#
# stu1=OldboyStudent('猪哥',19,'male',1)
# print(stu1.__dict__)
#
# print(OldboyStudent.mro())


class A:
    def f1(self):
        print('A.f1')

class B:
    def f2(self):
        super().f1()
        print('B.f2')

class C(B,A):
    pass

obj=C()
print(C.mro()) #C-》B->A->object
obj.f2()






