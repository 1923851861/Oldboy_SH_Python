'''
面向过程编程
    核心过程二字，过程指的是解决问题的步骤，即先干什么、再干什么、然后干什么...
    基于该思想编写程序就好比在设计一条流水线，是一种机械式的思维方式

    优点
        复杂的问题流程化、进而简单化
    缺点
        扩展性极差

'''

# 接收用户输入用户名,进行用户名合法性校验，拿到合法的用户名
def check_user():
    while True:
        name = input('username>>').strip()
        if name.isalpha():
           return name
        else:
            print('用户名必须为字母，傻叉')

# 接收用户输入密码,进行密码合法性校验，拿到合法的密码
def check_pwd():
    while True:
        pwd1=input('password>>: ').strip()
        if len(pwd1) < 5:
            print('密码的长度至少5位')
            continue
        pwd2=input('again>>: ').strip()
        if pwd1 == pwd2:
            return pwd1
        else:
            print('两次输入的密码不一致')

def check_age():
    pass

# pwd=check_pwd()
# print(pwd)
# 将合法的用户名与密码写入文件
def insert(user,pwd,age,path='db.txt'):
    with open(path,mode='a',encoding='utf-8') as f:
        f.write('%s:%s:%s\n' %(user,pwd,age))

def register():
    user=check_user()
    pwd=check_pwd()
    age=check_age()
    insert(user,pwd,age)
    print('register successfull')

register()



# 用户功能层
def register():
    while True: # 检测用户名
        name=input('username>>: ').strip()
        #检测用户是否重复，如果重复了则重新输入，否则break
        res=check_user_interface(name)
        if res:
            print('用户存在')
        else:
            break

    while True: # 检测密码
        pwd1 = input('pwd1>>: ').strip()
        pwd2 = input('pwd2>>: ').strip()
        if pwd1 != pwd2:
            print('两次输入密码不一致，重新输入')
        else:
            break


def tell_info():
    name=input('>>: ').strip()
    info=select(name)
    print(info)

# 接口层
def check_user_interface(name):
    res = select(name)  # res=['egon','123']
    if res:
        return True
    else:
        return False


# 数据处理层
def select(name):
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            info = line.strip('\n').split(':') #info=['egon','123']
            if name == info[0]:
                return info










