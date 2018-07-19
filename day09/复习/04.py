# #注册功能
# uname=input('name>>:').strip()
# pwd=input('password>>:').strip()
# pwd1=input('请重复输入密码>>:').strip()
# with open('db.txt','at',encoding='utf-8')as f:
#     if pwd==pwd1:
#         f.write('%s:%s\n' %(uname,pwd1))

# 认证功能
# inp_uname = input('请输入账号>>:：').strip()
# inp_pwd = input('请输入密码>>:：').strip()
# with open('db.txt', 'rt', encoding='utf-8')as f:
#     for line in f:
#         info = line.strip('\n').split(':')
#         if inp_uname == info[0] and inp_pwd == info[1]:
#             print('恭喜你，登陆成功！！')
#             break
#     else:
#         print('你是猪吗？输错啦！！')


def check_user():
    while True:
        uname = input('name>>:').strip()
        if uname.isalpha():
            return uname
        else:
            print('用户名由字母组成')
        # pwd = input('password>>:').strip()


def check_pwd():
    while True:
        pwd = input('password>>:').strip()
        pwd1 = input('请重复输入密码>>:').strip()
        if pwd1 == pwd:
            return pwd
        else:
            print('两次密码输的不一样，白痴！！')


def db_hanle(uname, pwd1):
    with open('db.txt', 'at', encoding='utf-8')as f:
        f.write('%s:%s\n' % (uname, pwd1))
        f.flush()


# 函数：注册功能
def register():
    x = check_user()  # 检测用户名是否合法
    y = check_pwd()  # 检测密码是否合法
    db_hanle(x, y)  # 写入数据文件

register()


# 函数：认证模式
# def aut():
#     inp_uname = input('请输入账号>>:：').strip()
#     inp_pwd = input('请输入密码>>:：').strip()
#     with open('db.txt', 'rt', encoding='utf-8')as f:
#         for line in f:
#             info = line.strip('\n').split(':')
#             if inp_uname == info[0] and inp_pwd == info[1]:
#                 print('恭喜你，登陆成功！！')
#                 break
#         else:
#             print('你是猪吗？输错啦！！')
#
# register()
# aut()
