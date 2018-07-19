# 面向对象作业
# 	1、类的属性和对象的属性有什么区别?
#     类的属性每个对象都有，如果类的属性变了，对象对应该属性的值也会变。
#     对象的属性，是该对象自己独有的，其他对象是访问不到的。对象在找属性的时候，首先先从自己的名称空间里找，找不到再去类的名称空间查找，
#     再找不到的话，程序就会出错。
# 	2、面向过程编程与面向对象编程的区别与应用场景?
#      面向过程编程：是按照过程来进行编程，具体分成几个步骤，先做什么，再做什么，然后再做什么。优点：程序简单化    缺点：扩展性差
#      面向对象编程：创造数一系列的对象，去进行数据的交互，解决问题。 优点：程序扩展性强    缺点：程序复杂
# 	3、类和对象在内存中是如何保存的。
#      在定义类的时候，创造出一个类的名称空间，将类体代码产生的名称放进名称空间里。
#      在类的实例化中，产生一个对象就是产生一个对象的名称空间，将对象独有的属性放进类的名称空间中
# 	4、什么是绑定到对象的方法，、如何定义，如何调用，给谁用？有什么特性
#
# class student:
#     school = '电子校'
#
#     def choice_class(self):
#         print('执行选课功能')
#
# st1 = student()
#
# st1.choice_class()


# 	5、如下示例, 请用面向对象的形式优化以下代码
# 	   在没有学习类这个概念时，数据与功能是分离的,如下
'''
def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx
def exc2(host,port,db,charset,proc_name)
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx
# 	   # 每次调用都需要重复传入一堆参数
exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')


class foo:
    def __init__(self,host,port,db,charset):
        self.host = host
        self.port = port
        self,db = db
        self.charset = charset

    def exc1(self,sql):
        conn = connect(self.host, self.port, self.db, self.charset)
        conn.execute(sql)
        return xxx
    def exc2(self,proc_name):
        conn = connect(self.host, self.port, self.db, self.charset)
        conn.call_proc(sql)
        return xxx
foo1 = foo('127.0.0.1',3306,'db1','utf8')
foo1.exc1('select * from tb1;')
foo1.exc2('存储过程的名字')
'''
# 5 下面这段代码的输出结果将是什么？请解释。
# class Parent(object):
#    x = 1
#
# class Child1(Parent):
#    pass
#
# class Child2(Parent):
#    pass
# #
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)

#       '1,1,1'
#       '1,2,1'
#       '3,2,3'
# 7、定义学校类，实例化出：北京校区、上海校区两个对象
# 		校区独有的特征有：
# 			校区名=“xxx”
# 			校区地址={'city':"所在市",'district':'所在的区'}
# 			多们课程名=['xxx','yyy','zzz']
# 			多个班级名=['xxx','yyy','zzz']
#
# 		校区可以：
# 			1、创建班级
# 			2、查看本校区开设的所有班级名
# 			3、创建课程
# 			4、查看本校区开设的所有课程名

# class OldSchool:
#     def __init__(self, school, city, area):
#         self.school = school
#         self.adds = {'city': city, 'district': area}
#         self.course = []
#         self.the_class = []

#     def setup_class(self, the_class):
#         self.the_class.append(the_class)
#         # print('班级创建成功')

#     def setup_course(self, course):
#         self.course.append(course)
#         # print('课程创建成功')
#
# sc1 = OldSchool('上海校区','上海市','浦东新区')
# sc1.setup_class('python脱产二期')
# sc1.setup_class('python脱产三期')
# sc1.setup_class('python周末三期')
# sc1.setup_course('Python课程')
# sc1.setup_course('Linux课程')
#
# print(sc1.school,sc1.adds)
# print(sc1.course)
# print(sc1.the_class)


# 8、定义出班级类，实例化出两个班级对象
# 		班级对象独有的特征：
# 			班级名=‘xxx’
# 			所属校区名=‘xxx’
# 			多门课程名=['xxx','yyy','zzz']
# 			多个讲师名=['xxx','xxx','xxx']
#
# 		班级可以：
# 			1、查看本班所有的课程
# 			2、查看本班的任课老师姓名
#
# class Macc:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.course = []
#         self.teacher = []
#
#     def set_course(self, course):
#         self.course.append(course)
#
#     def set_teacher(self, teacher):
#         self.teacher.append(teacher)
#
# ma1 = Macc('脱产二期','上海校区')
# ma1.set_course('xxx')
# ma1.set_course('yyy')
# ma1.set_course('zzz')
# ma1.set_teacher('egon')
# ma1.set_teacher('cxx')
# ma1.set_teacher('lxx')
# print(ma1.course)
# print(ma1.teacher)

# 	9、定义课程类，实例化出python、linux、go三门课程对象
# 		课程对象独有的特征：
# 			课程名=‘xxx’
# 			周期=‘3mons’
# 			价格=3000
#
# 		课程对象可以：
# 			1、查看课程的详细信息

# class Course:
#
#     def __init__(self,course):
#         self.name = course
#         self.weeks = '3mons'
#         self.price = '3000'
#
# c1 = Course('python')
# c2 = Course('linux')
# c3 = Course('go')
#
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)

# 	10、定义学生类，实例化出张铁蛋、王三炮两名学生对象
# 		学生对象独有的特征：
# 			学号=10
# 			名字=”xxx“
# 			班级名=['xxx','yyy']
# 			分数=33
#
# 		学生可以：
# 			1、选择班级
# 			3、注册，将对象序列化到文件
# import pickle
# class Bj:
#     group = ['python脱产班','linux脱产班']
#
#
# class Guy:
#     def __init__(self,id_name,name):
#         self.id_name = id_name
#         self.name = name
#         self.the_class = []
#         self.score = 33
#
#     def choice_class(self,group):
#         # print('''
#         #     1 python脱产班
#         #     2 linux脱产班
#         # ''')
#         # choice = input('请选择你要选择的课程')
#         # if choice == '1':
#         #     self.the_class.append('python脱产班')
#         #     print('选课成功')
#         # elif choice == '2':
#         #     self.the_class.append('linux脱产班')
#         #     print('选课成功')
#         while True:
#             for i,items in enumerate(group):
#                 print(i,items)
#             choice = input('请选择>>:').strip()
#             if choice.isdigit():
#                 choice = int(choice)
#             if choice > len(group):continue
#             self.the_class.append(group[choice])
#             with open('%s_pickle' %self.name,'wb') as f:
#                 pickle.dump(self,f)
#             print('选课成功')
#             break
#
# id_name = input('请输入学号').strip()
# name = input('请输入姓名').strip()
# g1 = Guy(id_name,name,)
# g1.choice_class(Bj.group)
# print(g1.__dict__)

# 11、定义讲师类，实例化出egon，lqz，alex，wxx四名老师对象
# 		老师对象独有的特征：
# 			名字=“xxx”
# 			等级=“xxx”、
# 		老师可以：
# 			1、修改学生的成绩
# class Bj:
#     group = ['python脱产班','linux脱产班']

class Guy:
    def __init__(self,id_name,name):
        self.id_name = id_name
        self.name = name
        self.the_class = []
        self.score = 33

class Teacher:
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def foo(self,st,new):
        st.score = new
g1 = Guy('2015130704','zhu')
t1 = Teacher('egon',10)
t2 = Teacher('lqz',9)
t3 = Teacher('alex',8)
t4 = Teacher('wxx',7)

t1.foo(g1,100)
print(g1.score)

# 	12、用面向对象的形式编写一个老师类, 老师有特征：编号、姓名、性别、年龄、等级、工资，老师类中有功能
# 		1、生成老师唯一编号的功能，可以用hashlib对当前时间加上老师的所有信息进行校验得到一个hash值来作为老师的编号
# 			def create_id(self):
# 				pass
# 		2、获取老师所有信息
# 			def tell_info(self):
# 				pass
#
# 		3、将老师对象序列化保存到文件里，文件名即老师的编号，提示功能如下
# 			def save(self):
# 				with open('老师的编号','wb') as f:
# 					pickle.dump(self,f)
#
# 		4、从文件夹中取出存储老师对象的文件，然后反序列化出老师对象,提示功能如下
# 			def get_obj_by_id(self,id):
# 				return pickle.load(open(id,'rb'))

# import pickle, hashlib, datetime
#
#
# class Teachers:
#     def __init__(self, name, sex, age, level, wage):
#         self.id_name = ''
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.level = level
#         self.wage = wage
#
#     def create_id(self):
#         m = hashlib.md5()
#         t1 = datetime.datetime.now()
#         m.update(t1)
#         m.update(self)
#         info = m.hexdigest
#         return info
#
#     def save(self):
#         with open(self.id_name, 'wb') as f:
#             pickle.dump(self, f)
#
#     def get_obj_by_id(self, id):
#         return pickle.load(open(id, 'rb'))
#
# t1 = Teachers('zcy','male',19,8,5000)
# n = t1.create_id()
