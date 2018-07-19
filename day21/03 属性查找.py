class OldboyStudent:
    school='oldboy'
    count=0

    def __init__(self, x, y, z): #会在调用类时自动触发
        self.name = x #stu1.name='耗哥'
        self.age = y  #stu1.age=18
        self.sex = z #stu1.sex='male'
        OldboyStudent.count+=1

    def choose_course(self):
        print('is choosing course')


# 先从对象自己的名称空间找，没有则去类中找，如果类也没有则报错
stu1=OldboyStudent('耗哥',18,'male')
stu2=OldboyStudent('猪哥',17,'male')
stu3=OldboyStudent('帅翔',19,'female')

print(OldboyStudent.count)
print(stu1.count)
print(stu2.count)
print(stu3.count)
