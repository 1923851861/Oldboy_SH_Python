# 面向对象作业
# 	1、类的属性和对象的属性有什么区别?
# 	2、面向过程编程与面向对象编程的区别与应用场景?
# 	3、类和对象在内存中是如何保存的。
# 	4、什么是绑定到对象的方法，、如何定义，如何调用，给谁用？有什么特性
# 	5、如下示例, 请用面向对象的形式优化以下代码
# 	   在没有学习类这个概念时，数据与功能是分离的,如下
# 	   def exc1(host,port,db,charset):
# 	   conn=connect(host,port,db,charset)
# 	   conn.execute(sql)
# 	   return xxx
# 	   def exc2(host,port,db,charset,proc_name)
# 	   conn=connect(host,port,db,charset)
# 	   conn.call_proc(sql)
# 	   return xxx
# 	   # 每次调用都需要重复传入一堆参数
# 	   exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
# 	   exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')
#
# 	6、下面这段代码的输出结果将是什么？请解释。
# 		class Parent(object):
# 		   x = 1
#
# 		class Child1(Parent):
# 		   pass
#
# 		class Child2(Parent):
# 		   pass
#
# 		print(Parent.x, Child1.x, Child2.x)
# 		Child1.x = 2
# 		print(Parent.x, Child1.x, Child2.x)
# 		Parent.x = 3
# 		print(Parent.x, Child1.x, Child2.x)
#
# 	7、定义学校类，实例化出：北京校区、上海校区两个对象
# 		校区独有的特征有：
# 			校区名=“xxx”
# 			校区地址={'city':"所在市",'district':'所在的区'}
# 			多个课程名=['xxx','yyy','zzz']
# 			多个班级名=['xxx','yyy','zzz']
#
# 		校区可以：
# 			1、创建班级
# 			2、查看本校区开设的所有班级名
# 			3、创建课程
# 			4、查看本校区开设的所有课程名

# class School:
#     def __init__(self,school,city,area):
#         self.school=school
#         self.add={'city':city,'area':area}
#         self.the_course=[]
#         self.the_class=[]
#     def choose_course(self,the_course):
#         self.the_course.append(the_course)
#     def choose_class(self,the_class):
#         self.the_class.append(the_class)
#
# sch1=School('北京校区','北京','五环')
# sch1.choose_course('python全栈开发课程')
# sch1.choose_course('linux课程')
# sch1.choose_class('脱产一期')
# sch1.choose_class('脱产二期')
#
# print(sch1.school,sch1.add,sch1.the_class,sch1.the_course)

#
#
# 	8、定义出班级类，实例化出两个班级对象
# 		班级对象独有的特征：
# 			班级名=‘xxx’
# 			所属校区名=‘xxx’
# 			多门课程名=['xxx','yyy','zzz']
# 			多个讲师名=['xxx','xxx','xxx']
#
# 		班级可以：
# 			1、查看本班所有的课程
# 			2、查看本班的任课老师姓名

# class the_class:
#     def __init__(self,class_name,school_name):
#         self.class_name=class_name
#         self.school_name=school_name
#         self.course_name=[]
#         self.teacher_name=[]
#     def choose_course(self,course_name):
#         self.course_name.append(course_name)
#     def choose_teacher(self,teacher_name):
#         self.teacher_name.append(teacher_name)

# class1=the_class('第三班级','上海校区')
# class1.choose_course('全栈开发一期')
# class1.choose_course('全栈开发二期')
# class1.choose_teacher('egon')
# class1.choose_teacher('alex')
# class1.choose_teacher('wxx')
#
# print(class1.class_name,class1.school_name)
# print(class1.course_name)
# print(class1.teacher_name)


# 	9、定义课程类，实例化出python、linux、go三门课程对象
# 		课程对象独有的特征：
# 			课程名=‘xxx’
# 			周期=‘3mons’
# 			价格=3000
#
# 		课程对象可以：
# 			1、查看课程的详细信息

# class course:
#     def __init__(self,name,period,price):
#         self.the_name = name
#         self.period=period
#         self.price=price
#
#     def tell_info(self):
#         print('''
#         课程名=%s
#         周期=%s
#         价格=%s
#         '''%(self.the_name,self.period,self.price))
#
#
#
#
# c1=course('python','5.5mons','10000')
# c2=course('linux','3mons','1000')
# c3=course('go','1mons','100')
# print(c1.tell_info())
# print(c2.tell_info())
# print(c3.tell_info())

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
# class Student:
#     def __init__(self,id,name,the_class,score):
#         self.id=id
#         self.name=name
#         self.the_class=[]
#         self.score=score
#     def choose_class(self,the_class):
#         self.the_class.append(the_class)


#
# 	11、定义讲师类，实例化出egon，lqz，alex，wxx四名老师对象
# 		老师对象独有的特征：
# 			名字=“xxx”
# 			等级=“xxx”、
# 		老师可以：
# 			1、修改学生的成绩



#
#
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
#
#
#
# 	13、按照定义老师的方式，再定义一个学生类
#
# 	14、抽象老师类与学生类得到父类，用继承的方式减少代码冗余
#
#
# 	15、基于面向对象设计一个对战游戏并使用继承优化代码，参考博客
# 		http://www.cnblogs.com/linhaifeng/articles/7340497.html#_label1