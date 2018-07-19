'''
面向过程编程：
    核心是过程二字，过程指的是解决问题的步骤，即想干什么再干什么后干什么。。。
    基于该思想编写程序就好比在设计一条流水线，是一种机械式的思维方式

    优点:
        复杂的问题流程化、进而简单化
    缺点：
        可扩展性差

面向对象编程：
    核心是对象二字，对象是特征与技能的结合体
    基于该思想在编写程序就好比在创造一个世界，世界万物都是对象，你就是这个世界的上帝


    对象是特征与技能的结合体,类就是一系列对象相似的特征与技能的结合体
    站在不同的角度，总结出的类是截然不同的

    在现实世界中一定是先有的一个个具体存在的对象，然后随着人类文明地发展而总结出了不同的类
    在程序中务必保证先定义类，后调用类来产生对象

    现实世界中总结对象-----》抽取相似之处，得到现实世界中的类---》定义为程序中的类-----》调用类，产生程序中的对象
    站在老男孩选课系统的角度：
        现实世界中的老男孩学生对象：
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
#1、先定义类
class OldboyStudent:
    school='oldboy'

    def choose_course(self):
        print('is choosing course')

#强调：类定义阶段会立刻执行类体代码，会产生类的名称空间，将类体代码执行过程中产生的名字都丢进去
# print(OldboyStudent.__dict__)
# 类本质就是一个名称空间/容器，从类的名称空间中增/删/改/查名字
# python为我们提供专门访问属性（名称空间中的名字）的语法，点后的都是属性
# OldboyStudent.school #OldboyStudent.__dict__['school']
# OldboyStudent.x=1 #OldboyStudent.__dict__['x']=1
# OldboyStudent.school='Oldboy' #OldboyStudent.__dict__['school']='Oldboy'
# del OldboyStudent.x #del OldboyStudent.__dict__['x']

# 类中定义的函数是类的函数属性，类可以使用，但使用的就是一个普通的函数而已，意味着需要完全遵循函数的参数规则，该传几个值就传几个
# OldboyStudent.choose_course(123)

#2、后调用类产生对象，调用类的过程称之为实例化，实例化的结果称为类的一个实例或者对象
stu1=OldboyStudent()
stu2=OldboyStudent()
stu3=OldboyStudent()
# print(stu1)
# print(stu2)
# print(stu3)

# print(OldboyStudent.school)
# OldboyStudent.school='OLDBOY'
# print(stu1.school)
# print(stu2.school)
# print(stu3.school)
