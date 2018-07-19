'''
# 例1
class OldboyStudent:
    school='oldboy'

    def choose_course(self):
        print('is choosing course')

stu1=OldboyStudent()
stu2=OldboyStudent()
stu3=OldboyStudent()

#对象本质也就是一个名称空间而已，对象名称空间是用存放对象自己独有的名字/属性，而
#类中存放的是对象们共有的属性
# print(stu1.__dict__)
# print(stu2.__dict__)
# print(stu3.__dict__)

stu1.name='耗哥'
stu1.age=18
stu1.sex='male'
# print(stu1.name,stu1.age,stu1.sex)
# print(stu1.__dict__)

stu2.name='猪哥'
stu2.age=17
stu2.sex='male'

stu3.name='帅翔'
stu3.age=19
stu3.sex='female'


# 例2
class OldboyStudent:
    school='oldboy'

    def choose_course(self):
        print('is choosing course')

stu1=OldboyStudent()
stu2=OldboyStudent()
stu3=OldboyStudent()

def init(obj,x,y,z):
    obj.name=x
    obj.age=y
    obj.sex=z

# stu1.name='耗哥'
# stu1.age=18
# stu1.sex='male'
init(stu1,'耗哥',18,'male')

# stu2.name='猪哥'
# stu2.age=17
# stu2.sex='male'
init(stu2,'诸哥',17,'male')

# stu3.name='帅翔'
# stu3.age=19
# stu3.sex='female'
init(stu3,'帅翔',19,'female')


print(stu1.__dict__)
print(stu2.__dict__)
print(stu3.__dict__)
'''


class OldboyStudent:
    school='oldboy'


    def __init__(obj, x, y, z): #会在调用类时自动触发
        obj.name = x #stu1.name='耗哥'
        obj.age = y  #stu1.age=18
        obj.sex = z #stu1.sex='male'

    def choose_course(self):
        print('is choosing course')

#调用类时发生两件事
#1、创造一个空对象stu1
#2、自动触发类中__init__功能的执行，将stu1以及调用类括号内的参数一同传入
stu1=OldboyStudent('耗哥',18,'male') #OldboyStudent.__init__(stu1,'耗哥',18,'male')
stu2=OldboyStudent('猪哥',17,'male')
stu3=OldboyStudent('帅翔',19,'female')


print(stu1.__dict__)
print(stu2.__dict__)
print(stu3.__dict__)
