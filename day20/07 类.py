'''
类：种类、分类、类别
    对象是特征与技能的结合体，类是一系列对象相似的特征与技能的结合体
    强调：站的角度不同，总结出的类是截然不同的

    在现实世界中：先有的一个个具体存在的对象，然后随着人类文明的发展才了分类的概念
    在程序中：必须先定义类，后调用类来产生对象

站在老男孩选课系统的角度，先总结现实世界中的老男孩的学生对象
    对象1：
        特征：
            学校='oldboy'
            姓名='耗哥'
            年龄=18
            性别='male'
        技能：
            选课

    对象2：
        特征：
            学校='oldboy'
            姓名='猪哥'
            年龄=17
            性别='male'
        技能：
            选课

    对象3：
        特征：
            学校='oldboy'
            姓名='帅翔'
            年龄=19
            性别='female'
        技能：
            选课

站在老男孩选课系统的角度，先总结现实世界中的老男孩学生类
    老男孩学生类：
        相似的特征：
            学校='oldboy'
        相似的技能
            选课
'''
#在程序中
#   1、先定义类
class OldboyStudent:
    school='oldboy'

    def choose_course(self):
        print('is choosing course')

#类体代码会在类定义阶段就立刻执行，会产生一个类的名称空间

# 类的本身其实就是一个容器/名称空间，是用来存放名字的，这是类的用途之一
# print(OldboyStudent.__dict__)#查看类的名称空间
# print(OldboyStudent.__dict__['school'])
# print(OldboyStudent.__dict__['choose_course'])
# OldboyStudent.__dict__['choose_course'](111)

# print(OldboyStudent.school) #OldboyStudent.__dict__['school']
# print(OldboyStudent.choose_course) #OldboyStudent.__dict__['choose_course']

# OldboyStudent.choose_course(111)

# OldboyStudent.country='China' #OldboyStudent.__dict__['country']='China'
# OldboyStudent.country='CHINA' #OldboyStudent.__dict__['country']='China'
# del OldboyStudent.school
# print(OldboyStudent.__dict__)



#   2、后调用类产生对象,调用类的过程，又称为类的实例化，实例化的结果称为类的对象/实例
# stu1=OldboyStudent() # 调用类会得到一个返回值，该返回值就是类的一个具体存在的对象/实例
# stu2=OldboyStudent() # 调用类会得到一个返回值，该返回值就是类的一个具体存在的对象/实例
# stu3=OldboyStudent() # 调用类会得到一个返回值，该返回值就是类的一个具体存在的对象/实例

# 类的实例化过程都发生了哪些事？
# 如何在实例化的过程中为对象定制自己独有的特征
# 程序中对象到底是什么，如何使用？



