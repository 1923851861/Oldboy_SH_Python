class OldboyStudent:
    school='oldboy'


    def __init__(self, x, y, z): #会在调用类时自动触发
        self.name = x #stu1.name='耗哥'
        self.age = y  #stu1.age=18
        self.sex = z #stu1.sex='male'

    def choose_course(self,x):
        print('%s is choosing course' %self.name)

    def func():
        pass
# 类名称空间中定义的数据属性和函数属性都是共享给所有对象用的
# 对象名称空间中定义的只有数据属性，而且时对象所独有的数据属性

stu1=OldboyStudent('耗哥',18,'male')
stu2=OldboyStudent('猪哥',17,'male')
stu3=OldboyStudent('帅翔',19,'female')

# print(stu1.name)
# print(stu1.school)


# 类中定义的函数是类的函数属性，类可以使用，但使用的就是一个普通的函数而已，意味着需要完全遵循函数的参数规则，该传几个值就传几个
# print(OldboyStudent.choose_course)
# OldboyStudent.choose_course(123)

# 类中定义的函数是共享给所有对象的，对象也可以使用，而且是绑定给对象用的，
#绑定的效果：绑定给谁，就应该由谁来调用，谁来调用就会将谁当作第一个参数自动传入
# print(id(stu1.choose_course))
# print(id(stu2.choose_course))
# print(id(stu3.choose_course))
# print(id(OldboyStudent.choose_course))

# print(id(stu1.school))
# print(id(stu2.school))
# print(id(stu3.school))
#
# print(id(stu1.name),id(stu2.name),id(stu3.name))


# stu1.choose_course(1)
# stu2.choose_course(2)
# stu3.choose_course(3)
stu1.func()

# 补充：类中定义的函数，类确实可以使用，但其实类定义的函数大多情况下都是绑定给对象用的，所以在类中定义的函数都应该自带一个参数self

