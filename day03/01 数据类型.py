'''
1、什么是数据类型
    变量值才是我们存储的数据，所以数据类指的就是变量值的不同种类

2、为何数据要分类型？
    变量值是用来保存现实世界中的状态的，那么针对不同的状态就应该用不同类型的数据去表示


3、如何用，即数据类型的分类？

'''
#一：数字类型
#整型int
#1、作用：表示人的年龄、各种号码、等级

#2、定义
# age=18 #age=int(18)
#
# print(id(age))
# print(type(age))
# print(age)

#3、如何用


#二、浮点型float
#1、作用：表示身高、体重、薪资。。。

#2、定义
# salary=3.1 #salary=float(3.1)
# print(id(salary))
# print(type(salary))
# print(salary)

#3、如何用


#三、字符串类型str
#1、作用：表示描述性质的状态，比如人的名字，家庭住址

#2、定义:在单引号、双引号、三引号内包含的一串字符
# name='egon' #name=str('egon' )

# msg='''
# alex
# egon
# wxx
# '''
# print(type(name))
# print(type(msg))

#注意点：
# msg="my name is 'egon'"
# print(msg)

#3、如何用
#字符串类型只能：+或者*
# msg='hello'
# name='egon'
#
# print(msg + name)

# name='egon'
# print(name * 10)
#
# print(1)
# print(2)
# print(3)
# print('-'*100)
# print(1)
# print(2)
# print(3)
#

# msg1='zaello '
# msg2='za'


# print(msg2 > msg1)

# print('a' > 'Z')


# 四:列表list
#1、作用：用来存取放多个值

#2、如何定义:在[]内用逗号分隔开多个任意类型的值
# l=[1,'a',3.1,[1,3]] #l=list([1,'a',3.1,[1,3]])
# print(id(l))
# print(type(l))
# print(l)
# x=111
# l=[1,2,x,'a']
# print(l)

# hobbies=['read','run','basketball']
        # 0      1      2
#3、如何用:按照索引取值，索引是从0开始的
# print(hobbies[2]) #
# print(hobbies)


# l=['alex','male',['oldboy',200]]
# print(l[2][1])
#
# #练习
students_info=[['egon',18,['play',]],['alex',18,['play','sleep']]]
# #取出第一个学生的第一个爱好
# print(students_info[0][2][0])
#






# 五:字典dict
#1、作用：用来存取放多个值，按照key：value的方式存放的值，取的时候可以通过key而非索引去取值，key对value是有描述性功能的


#2、定义方式：在{}内用逗号分隔开多个元素，每一个元素都是key:value的格式，其中value可以是任意类型，key大多数情况都是字符串类型
          # 'name' 'sex' 'age'  'company_info'
# user_info=['egon','male',18,['oldboy','Shanghai',20]]

# print(user_info[1])
# print(user_info[0])
# print(user_info[3][1])


          # 'name' 'sex' 'age'  'company_info'
# user_info={
#     'name':'egon',
#     'sex':'male',
#     'age':18,
#     'company_info':{'c_name':'oldboy','c_addr':'Shanghai','members':20}
# }
#
# print(id(user_info))
# print(type(user_info))
# print(user_info)
#
# # print(user_info['name'])
# print(user_info['company_info']['c_name'])
#
# #练习
# students=[
#     {'name':'alex','age':38,'hobbies':['play','sleep']},
#     {'name':'egon','age':18,'hobbies':['read','sleep']},
#     {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
# ]
# print(students[1]['hobbies'][1])


# 六：布尔bool
#1、作用：用于判断的条件

#2、如何定义：True，False
# print(10 > 2 and 3 > 14)
# print(type(True))

# 所有的数据类型的值本身就是一种布尔值,即所有的数据类型都可以当作条件去用
# 在如此多的数据类型中只需要记住：0，None，空，它们三类的布尔值为False

# print(bool(0))
# print(bool(None))
# print(bool(''))
# print(bool([]))
# print(bool({}))
















