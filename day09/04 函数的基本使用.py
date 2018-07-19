'''


# 注册功能
uname=input('username>>：').strip()
pwd1=input('password>>: ').strip()
pwd2=input('重复输入密码>>: ').strip()
if pwd1 == pwd2:
    with open('db.txt','at',encoding='utf-8') as f:
        f.write('%s:%s\n' %(uname,pwd1))
        f.flush() #flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。

#认证功能
inp_uname=input('请输入你的账号：').strip()
inp_pwd=input('请输入你的密码：').strip()
with open('db.txt','rt',encoding='utf-8') as f:
    for line in f:
        info=line.strip('\n').split(':')
        if inp_uname == info[0] and inp_pwd == info[1]:
            print('login successfull')
            break
    else:
        print('账号或密码错误')

# 注册功能
uname=input('username>>：').strip()
pwd=input('password>>: ').strip()
with open('db.txt','at',encoding='utf-8') as f:
    f.write('%s:%s\n' %(uname,pwd))
    f.flush()

# 注册功能
uname=input('username>>：').strip()
pwd=input('password>>: ').strip()
with open('db.txt','at',encoding='utf-8') as f:
    f.write('%s:%s\n' %(uname,pwd))
    f.flush()

#认证功能
inp_uname=input('请输入你的账号：').strip()
inp_pwd=input('请输入你的密码：').strip()
with open('db.txt','rt',encoding='utf-8') as f:
    for line in f:
        info=line.strip('\n').split(':')
        if inp_uname == info[0] and inp_pwd == info[1]:
            print('login successfull')
            break
    else:
        print('账号或密码错误')

'''


'''
1、什么是函数？   
在程序中,函数就具备某一功能的工具
事先将工具准备好即函数的定义
遇到应用场景拿来就用即函数的调用
所以务必记住:#函数的使用必须遵循先定义,后调用的原则

2、为何要用函数
 不用函数问题是：
 1、程序冗长
 2 程序的扩展性差
 3 程序的可读性差

3 如何用函数:
  函数的使用必须遵循先定义,后调用的原则
'''
# def 函数名(参数1,参数2,...):
#     '''
#     函数功能的描述信息
#     :param 参数1: 描述
#     :param 参数2: 描述
#     :return: 返回值
#     '''
#     代码1
#     代码2
#     代码3
#     ...
#     return 返回值


# 准备好工具=>函数的定义阶段
def register():
    while True:
        uname=input('username>>：').strip()
        if uname.isalpha():
            break
        else:
            print('用户名必须由字母组成傻叉')

    while True:
        pwd1=input('密码>>: ').strip()
        pwd2=input('重复输入密码>>: ').strip()
        if pwd1 == pwd2:
            break
        else:
            print('两次输入的密码不一致,眼瞎吗')

    with open('db.txt','at',encoding='utf-8') as f:
        f.write('%s:%s\n' %(uname,pwd1))
        f.flush()

def auth():
    #认证功能
    inp_uname=input('请输入你的账号：').strip()
    inp_pwd=input('请输入你的密码：').strip()
    with open('db.txt','rt',encoding='utf-8') as f:
        for line in f:
            info=line.strip('\n').split(':')
            if inp_uname == info[0] and inp_pwd == info[1]:
                print('login successfull')
                break
        else:
            print('账号或密码错误')

# 拿来就用=>函数的调用阶段
# print(register)
# register()
# auth()
# register()
# register()
# register()


