# 总的分类：
# #1、形参：在函数定义阶段括号内定义的参数，称之为形式参数，简称形参，本质就是变量名
# def foo(x,y): #x=1,y=2
#     print(x)
#     print(y)
# #2、实参：在函数调用阶段括号内传入的值，称之为实际参数，简称实参，本质就是变量的值
# foo(1,2)
#

# 详细的分类：
# 一、位置参数：
# 位置形参：在函数定义阶段，按照从左到右的顺序依次定义的形参，称之为位置形参
# 特点：但凡是按照位置定义的形参，都必须被传值，多一个不行，少一个也不行
# def foo(x,y):
#     print('x:',x)
#     print('y:',y)


# 位置实参：在函数调用阶段，按照从左到右的顺序依次定义的实参，称之为位置实参
# # 特点：按照位置为对应的形参依次传值
# foo(1,2)
# foo(2,1)


# 二、关键字实参:在调用函数时，按照key=value的形式为指定的参数传值，称为关键字实参
# 特点：可以打破位置的限制，但仍能为指定的形参赋值
# foo(y=2,x=1)

# 注意：
# 1、可以混用位置实参与关键字实参，但位置实参必须放在关键字实参的前面
# foo(1,y=2)
# foo(y=2,1) #SyntaxError: positional argument follows keyword argument

# 2、可以混用，但不能对一个形参重复赋值
# foo(1,y=2,x=10)


# 三：默认参数：在函数定义阶段，就已经为形参赋值，该形参称为默认形参
# 特点：在定义阶段就已经被赋值，意味着在调用可以不用为其赋值
# def foo(x,y=10):
#     print('x:',x)
#     print('y:',y)

# foo(1)
# foo(1,3)
# 注意：
# 1、位置形参必须放到默认形参的前面，否则报语法错误
# def foo(x=1,y):
#     pass

# 2、默认参数的值只在定义阶段赋值一次，即默认参数的值在函数定义阶段就已经固定死了
# 即默认参数的值在函数定义阶段就已经固定死了#
# m=10
# def foo(x=m,y=11):
#     print(x)
#     print(y)
# m=1111111111111111111111111111111111111111111111111111111111
# foo()

# 3、默认参数的值通常应该定义不可变类型

# def register(name,hobby,hobbies=[]):
#     hobbies.append(hobby)
#     print('%s的爱好' %name,end=':')
#     print(hobbies)
#
# register('egon','play')
# register('alex','piao')
# register('lxx','烫头')

# def register(name,hobby,hobbies=None):
#     if hobbies is None:
#         hobbies=[]
#     hobbies.append(hobby)
#     print('%s的爱好' %name,end=':')
#     print(hobbies)
#
# register('egon','play')
# register('alex','piao')
# register('lxx','烫头')


# 总结：
# 实参的应用：取决于个人习惯，
# 形参的应用：
# 1、位置形参：大多数情况下的调用值都不一样，就应该将该参数定义成位置形参
# 2、默认形参：大多数情况下的调用值都一样，就应该将该参数定义成默认形参
# def register(name,age,sex='male'):
#     print(name)
#     print(age)
#     print(sex)
#
#
# register('egon',18,)
# register('大脑门',73,'female')
# register('小脑门',84,)
# register('大高个',18,)


# 四：可变长参数：指的是在调用函数时，传入的参数个数可以不固定
# 而调用函数时，传值的方式无非两种，一种位置实参，另一种时关键字实参
# 所以对应着，形参也必须有两种解决方案，来分别接收溢出的位置实参(*)与关键字实参(**)

# 1、形参中某个参数带*
# 形参中的*会将溢出的位置实参全部接收，然后存储元组的形式，然后把元组赋值给*后的变量名
# def foo(x,y,*z): #x=1,y=2,z=(3,4,5,6,7)
#     print(x)
#     print(y)
#     print(z)
# foo(1,2,3,4,5,6,7)

# 应用
# def my_sum(*nums):
#     res=0
#     for num in nums:
#         res+=num
#     return res
#
# print(my_sum(1,2,3,4,5))

# 2、实参中的参数也可以带*
# 实参中带*，*会将该参数的值循环取出，打散成位置实参
# ps：以后但凡碰到实参中带*的，它就是位置实参，应该立马打散成位置实参去看
# def foo(x,y,z):
#     print(x,y,z)
#
# foo(1,*[2,3]) #foo(1,2,3)
# foo(1,*'he') #foo(1,'h','e')
# foo(1,*(2,3,4)) #foo(1,2,3,4)

# def foo(x,y,z,*args):
#     print(x)
#     print(y)
#     print(z)
#     print(args)
#
# foo(1,2,3,4,5,6,7,*[8,9,10,11]) #foo(1,2,3,4,5,6,7,8,9,10,11)
# 注意：约定俗成形参中的*变量名的写法都是：*args


# 1、形参中某个参数带**
# 形参中的**会将溢出的关键字实参全部接收，然后存储字典的形式，然后把字典赋值给**后的变量名
# def foo(x,y,**z): #x=1,y=2,z={'c':5,'b':4,'a':3}
#     print(x)
#     print(y)
#     print(z)
# foo(1,2,a=3,b=4,c=5)

# 2、实参中的参数也可以带**,该参数必须是字典
# 实参中带**，**会将该参数的值循环取出，打散成关键字实参
# ps：以后但凡碰到实参中带**的，它就是关键字实参，应该立马打散成关键字实参去看
# def foo(x,y,z):
#     print(x)
#     print(y)
#     print(z)

# foo(1,2,**{'a':1,'b':2,'c':3,'z':3}) #foo(1,2,c=3,b=2,a=1,z=3)
# foo(**{'z':3,'x':1,'y':2}) #foo(y=2,x=1,z=3)

# 注意：约定俗成形参中的**变量名的写法都是：**kwargs

# def index(name,age,sex):
#     print('welecome %s:%s:%s to index page' %(name,age,sex))
#
# def wrapper(*args,**kwargs): #args=(1,),kwargs={'x': 1, 'y': 2, 'z': 3}
#     index(*args,**kwargs) #index(*(1,),**{'x': 1, 'y': 2, 'z': 3}) #index(1,x=1,y=2,z=3)
#
# wrapper(name='egon',sex='male',age=18)
#

# 五 命名关键字形参:在函数定义阶段，*后面的参数都是命名关键字参数(**)
# 特点：在传值时，必须按照key=value的传，并且key必须命名关键字参数指定的参数名
# def register(x,y,z,**kwargs): #kwargs={'b':18,'a':'egon'}
#     if 'name' not in kwargs or 'age' not in  kwargs:
#         print('用户名与年龄必须使用关键字的形式传值')
#         return
#     print(kwargs['name'])
#     print(kwargs['age'])
# register(1,2,3,a='egon',b=18)


# def register(x,y,z,*args,name='egon',age):
#     print(args)
#     print(name)
#     print(age)
# register(1,2,3,4,5,6,7,age=18)
#


# def foo(x,y=1,*args,z=1,a,b,**kwargs):
#     pass


# foo(1,*[1,2,3],a=1,**{'x':1,'y':2}) #foo(1,1,2,3,a=1,y=2,x=1)


# foo(1,2)
# foo(x=1,y=2)


# open('a.txt', 'w', encoding='utf-8')
