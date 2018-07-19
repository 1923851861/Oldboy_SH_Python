'''
1、什么是组合
    组合就是一个类的对象具备某一个属性，该属性的值是指向另外外一个类的对象


2、为何用组合
    组合也是用来解决类与类直接代码冗余问题的

3、如何用组合

class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class OldboyStudent(OldboyPeople):
    def __init__(self,name,age,sex,stu_id):
        OldboyPeople.__init__(self,name,age,sex)
        self.stu_id=stu_id

    def choose_course(self):
        print('%s is choosing course' %self.name)

class OldboyTeacher(OldboyPeople):

    def __init__(self, name, age, sex, level):
        OldboyPeople.__init__(self,name,age,sex)
        self.level=level

    def score(self,stu,num):
        stu.score=num
        print('老师[%s]为学生[%s]打分[%s]' %(self.name,stu.name,num))


stu1=OldboyStudent('猪哥',19,'male',1)
tea1=OldboyTeacher('egon',18,'male',10)

stu1.choose_course()
tea1.score(stu1,100)
print(stu1.__dict__)

'''


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_info(self):
        msg = """
        课程名：%s
        课程周期：%s
        课程价钱：%s
        """ % (self.name, self.period, self.price)
        print(msg)


class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyStudent(OldboyPeople):
    def __init__(self, name, age, sex, stu_id):
        OldboyPeople.__init__(self, name, age, sex)
        self.stu_id = stu_id

    def choose_course(self):
        print('%s is choosing course' % self.name)


class OldboyTeacher(OldboyPeople):

    def __init__(self, name, age, sex, level):
        OldboyPeople.__init__(self, name, age, sex)
        self.level = level

    def score(self, stu, num):
        stu.score = num
        print('老师[%s]为学生[%s]打分[%s]' % (self.name, stu.name, num))


# 创造课程
python = Course('python全栈开发', '5mons', 3000)
linux = Course('linux运维', '5mons', 800)
# python.tell_info()
# linux.tell_info()


# 创造学生与老师
stu1 = OldboyStudent('猪哥', 19, 'male', 1)
tea1 = OldboyTeacher('egon', 18, 'male', 10)

# 将学生、老师与课程对象关联/组合
stu1.course = python
tea1.course = linux

stu1.course.tell_info()
tea1.course.tell_info()
