#在python3中统一了类与类型的概念，类就是类型
class OldboyStudent:
    school='oldboy'

    def __init__(self, x, y, z): #会在调用类时自动触发
        self.name = x #stu1.name='耗哥'
        self.age = y  #stu1.age=18
        self.sex = z #stu1.sex='male'

    def choose_course(self,x):
        print('%s is choosing course' %self.name)

stu1=OldboyStudent('耗哥',18,'male')
# stu1.choose_course(1) #OldboyStudent.choose_course(stu1,1)
# OldboyStudent.choose_course(stu1,1)

[]
l=[1,2,3] #l=list([1,2,3])
# print(type(l))
# l.append(4) #list.append(l,4)
list.append(l,4)
print(l)

