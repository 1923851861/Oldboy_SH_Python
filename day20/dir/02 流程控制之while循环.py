#while语法,while循环又称为条件循环
# while 条件:
#     code1
#     code2
#     code3
#     ....


# user_db='egon'
# pwd_db='123'
#
# while True:
#     inp_user=input('username>>: ')
#     inp_pwd=input('password>>: ')
#     if inp_user == user_db and inp_pwd == pwd_db:
#         print('login successfull')
#     else:
#         print('user or password error')


#2 while+break:break的意思是终止掉当前层的循环,.执行其他代码
# while True:
#     print('1')
#     print('2')
#     break
#     print('3')

# user_db='egon'
# pwd_db='123'
#
# while True:
#     inp_user=input('username>>: ')
#     inp_pwd=input('password>>: ')
#     if inp_user == user_db and inp_pwd == pwd_db:
#         print('login successfull')
#         break
#     else:
#         print('user or password error')


# print('其他代码')

#3 while+continue:continue的意思是终止掉本次循环,.直接进入下一次循环
#ps:记住continue一定不要加到循环体最后一步执行的代码
# n=1
# while n <= 10: #
#     if n == 8:
#         n += 1 #n=9
#         continue
#     print(n)
#     n+=1 #n=11



# while True:
#     if 条件1:
#         code1
#         code2
#         code3
#         continue #无意义
#     elif 条件1:
#         code1
#         continue #有意义
#         code2
#         code3
#     elif 条件1:
#         code1
#         code2
#         code3
#         continue #无意义
#     ....
#     else:
#         code1
#         code2
#         code3
#         continue #无意义


#while循环嵌套
user_db='egon'
pwd_db='123'

while True:
    inp_user=input('username>>: ')
    inp_pwd=input('password>>: ')
    if inp_user == user_db and inp_pwd == pwd_db:
        print('login successfull')
        while True:
            cmd=input('请输入你要执行的命令: ')
            if cmd == 'q':
                break
            print('%s 功能执行...' %cmd)
        break
    else:
        print('user or password error')


print('end....')



#while+tag
user_db='egon'
pwd_db='123'

tag=True
while tag:
    inp_user=input('username>>: ')
    inp_pwd=input('password>>: ')
    if inp_user == user_db and inp_pwd == pwd_db:
        print('login successfull')
        while tag:
            cmd=input('请输入你要执行的命令: ')
            if cmd == 'q':
                tag=False
            else:
                print('%s 功能执行...' %cmd)

    else:
        print('user or password error')


print('end....')



#while+else (***)
n=1
while n < 5:
    # if n == 3:
    #     break
    print(n)
    n+=1
else:
    print('在整个循环结束后,会进行判断:只有while循环在没有被break结束掉的情况下才会执行else中的代码')


