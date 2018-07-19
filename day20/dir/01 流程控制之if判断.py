# 语法1
# if 条件:
#     代码1
#     代码2
#     代码3
#     ...

# cls='human'
# sex='female'
# age=18
#
# if cls == 'human' and sex == 'female' and age > 16 and age < 22:
#     print('开始表白')
#
# print('end....')
#
#

# 语法2
# if 条件:
#     代码1
#     代码2
#     代码3
#     ...
# else:
#     代码1
#     代码2
#     代码3
#     ...

# cls='human'
# sex='female'
# age=38
#
# if cls == 'human' and sex == 'female' and age > 16 and age < 22:
#     print('开始表白')
# else:
#     print('阿姨好')
#
# print('end....')


# 语法3
# if 条件1:
#     代码1
#     代码2
#     代码3
#     ...
# elif 条件2:
#     代码1
#     代码2
#     代码3
#     ...
# elif 条件3:
#     代码1
#     代码2
#     代码3
#     ...
# ............
# else:
#     代码1
#     代码2
#     代码3
#     ...


'''
如果：成绩>=90，那么：优秀

如果成绩>=80且<90,那么：良好

如果成绩>=70且<80,那么：普通

其他情况：很差

'''

# score=input('your score: ') #score='73'
# score=int(score) #score=73
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 70:
#     print('普通')
# else:
#     print('很差')


# user_from_db='egon'
# pwd_from_db='123'
#
# user_from_inp=input('username>>>: ')
# pwd_from_inp=input('password>>>: ')
#
# if user_from_inp == user_from_db and pwd_from_inp == pwd_from_db:
#     print('login successfull')
# else:
#     print('user or password error')



#if的嵌套

cls='human'
sex='female'
age=18
is_success=False

if cls == 'human' and sex == 'female' and age > 16 and age < 22:
    print('开始表白...')
    if is_success:
        print('在一起')
    else:
        print('我逗你玩呢....')
else:
    print('阿姨好')

print('end....')








