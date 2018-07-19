# 定义函数时的参数就是函数体接收外部传值的一种媒介，其实就一个变量名

# 1、无参函数：
# 在函数定义阶段括号内没有参数，称为无参函数
# 注意：定义时无参，意味着调用时也无需传入参数
# 应用：
# 如果函数体代码逻辑不需要依赖外部传入的值，必须定义无参函数

# def func():
#     print('hello world')
# func()


# 2、有参函数
# 在函数定义阶段括号内有参数，称为有参函数
# 注意：定义时有参，意味着调用时也必须传入参数
# 应用：
# 如果函数体代码逻辑需要依赖外部传入的值，必须定义成有参函数
# def sum2(x,y):
#     # x=10
#     # y=20
#     res=x+y
#     print(res)
#
# sum2(10,20)
# sum2(30,40)

def check_user():
    while True:
        uname = input('username>>：').strip()
        if uname.isalpha():
            return uname
            # break
        else:
            print('用户名必须由字母组成傻叉')


def check_pwd():
    while True:
        pwd1 = input('密码>>: ').strip()
        pwd2 = input('重复输入密码>>: ').strip()
        if pwd1 == pwd2:
            return pwd1
        else:
            print('两次输入的密码不一致,眼瞎吗')


def db_hanle(uname, pwd1):
    with open('db.txt', 'at', encoding='utf-8') as f:
        f.write('%s:%s\n' % (uname, pwd1))
        f.flush()


def register():
    # 检测用户名是否合法
    x = check_user()  # x='EGON'
    # 检测密码是否合法
    y = check_pwd()  # y='123'

    # 写入数据文件
    # db_hanle(合法的用户名，合法的密码)
    db_hanle(x, y)


# register()


# 3、空函数
#
# # def func():
# #     pass
#
#
# # def check_user():
# #     pass
# #
# #
# # def check_pwd():
# #     pass
# #
# #
# # def write_db(x, y):
# #     pass
# #
# #
# # def register():
# #     # 1 输入用户名，并进行合法性校验
# #     # 2 输入密码，并进行合法性校验
# #     # 3 将合法的用户名、密码写入文件
# #     x = check_user()
# #     y = check_pwd()
# #     write_db(x, y)