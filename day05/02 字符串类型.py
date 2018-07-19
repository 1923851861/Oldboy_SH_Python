#一：基本使用
# 1 用途: 描述性质的数据,比如人的名字,单个爱好,地址
#
# 2 定义方式
# name='egon' #name=str('egon')
# x=str(1)
# y=str(1.1)
# z=str([1,2,3])
# n=str({'a':1})
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(n))

# 3 常用操作+内置的方法
#优先掌握的操作(*****)：
#1、按索引取值(正向取+反向取) ：只能取
msg='hello world'
# print(type(msg[5]))
# print(msg[-1])
# msg[2]='A'

#2、切片(顾头不顾尾，步长)
msg='hello world'
# print(msg[1:5],type(msg[1:5]))
# print(msg[6:-1])
# print(msg[6:11])
# print(msg[6:])
# print(msg[6::2])
# 了解(**)

# print(msg[0:])
# print(msg[::-1])
# msg='hello world'
# print(msg[-3:-6:-1])
# print(msg[6:9:-1])

#3、长度len
# msg='hello world'
# print(len(msg))

#4、成员运算in和not in
# print('SB' in  'my name is alex,alex is SB')
# print('alex' in  'my name is alex,alex is SB')
# print('egon' not in  'my name is alex,alex is SB') # 推荐
# print(not 'egon' in  'my name is alex,alex is SB')


#5、移除空白strip
# name='  e gon        '
# print(name.strip(' '))
# print(name.strip())
# name='****A*e*gon****'
# print(name.strip('*'))

# name='****egon****'
# print(name.lstrip('*'))
# print(name.rstrip('*'))
# pwd=input('>>: ').strip() #pwd='123  '
# if pwd == '123':
#     print('login successful')


# msg='cccabcdefgccccc'
#          'c'
# print(msg.strip('c'))

# print('*-=egon *&^'.strip('-= *&^'))

#6、切分split
# msg='egon:18:male:180:160'
# l=msg.split(':')
# print(l)
# print(l[3])
#7、循环
# msg='hello world'
# for x in msg:
#     print(x)

# 需要掌握的操作(****)
#1、strip,lstrip,rstrip
#2、lower,upper
# name='EoN'
# print(name.lower())

# name='egonN'
# print(name.upper())

#3、startswith,endswith
# print('alex is SB'.startswith('alex'))
# print('alex is SB'.endswith('B'))

#4、format的三种玩法
# print('my name is %s my age is %s' %('egon',18))
# print('my name is {name} my age is {age}'.format(age=18,name='egon')) # 可以打破位置的限制,但仍能指名道姓地为指定的参数传值

# print('my name is {} my age is {}'.format('egon',18))
# print('my name is {0} my age is {1} {1} {1} {1}'.format('egon',18))

#5、split,rsplit
# info='egon:18:male'
# print(info.split(':',1))

# print(info.split(':',1)) #['egon','18:male']
# print(info.rsplit(':',1)) #['egon:18','male']

#6、join:只能将元素全为字符串的列表拼成一个大的字符串
# info='egon:18:male'
# l=info.split(':')
# print(l)
# new_info='-'.join(l)
# print(new_info)

# num=['a','b','c']
# new_num=':'.join(num) #'a'+':'+'b'+':'+'c'
# print(new_num)

# num=[1,2,'c']
# ':'.join(num) #1+':'+2+':'+'c'

#7、replace
# msg='my name is wupeiqi,wupeiqi is SB'
# print(msg.replace('wupeiqi','Pig',1))
# print(msg)

#8、isdigit
# print('111.1'.isdigit())
# print('1111'.isdigit())

# AGE=73
# age=input('>>: ').strip() #age='asdfasdf'
# if age.isdigit():
#     age=int(age)
#     if age > AGE:
#         print('too big')
#     elif age < AGE:
#         print('too small')
#     else:
#         print('you got it')
# else:
#     print('必须输入数字啊傻叉')

# 其他操作（了解即可）(**)
#1、find,rfind,index,rindex,count
# msg='my name is alex,alex is hahaha'
# print(msg.find('alex'))
# print(msg.find('SB')) #找不到会返回-1

# print(msg.index('alex'))
# print(msg.index('SB')) # 找不到index会报错

# print(msg.find('alex',0,3))

# print(msg.count('alex'))
# print(msg.count('alex',0,15))

#2、center,ljust,rjust,zfill
# print('info egon'.center(50,'-'))
# print('info egon'.ljust(50,'-'))
# print('info egon'.rjust(50,'-'))
# print('info egon'.zfill(50))

# 3、expandtabs
# print('a\tb\tc'.expandtabs(1))

#4、captalize,swapcase,title
# print('my name is egon'.capitalize())
# print('my Name Is egon'.swapcase())
# print('my name is egon'.title())

#5、is数字系列
num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3='壹' #中文数字
num4='Ⅳ' #罗马数字

#isdigit():bytes,unicode
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())

#isdecimal():unicode
# print(num2.isdecimal())
# print(num3.isdecimal())
# print(num4.isdecimal())

#isnumberic;unicode,中文,罗马
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())

#6、is其他
# print('abasdf123123'.isalnum())
# print('asdfasdf'.isalpha())
# print('egon'.islower())
# print('ABC'.isupper())

# print('     '.isspace())
# print('My Name Is Egon'.istitle())


# #二：该类型总结
# 1 存一个值or存多个值
#     只能存一个值
#
# 2 有序or无序
# 有序

# 3 可变or不可变
# 不可变

# name='egon'
# print(id(name))
# name='alex'
# print(id(name))