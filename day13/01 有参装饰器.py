'''

import time

current_user={'user':None}

def deco(func):
    def wrapper(*args,**kwargs):
        if current_user['user']:
            #已经登陆过
            res = func(*args, **kwargs)
            return res
        user=input('username>>: ').strip()
        pwd=input('password>>: ').strip()
        if user == 'egon' and pwd == '123':
            print('login successful')
            # 记录用户登陆状态
            current_user['user']=user
            res=func(*args,**kwargs)
            return res
        else:
            print('user or password error')
    return wrapper

@deco
def index():
    print('welcome to index page')
    time.sleep(1)

@deco
def home(name):
    print('welecome %s to home page' %name)
    time.sleep(0.5)


index()
home('egon')
'''

'''

def f1():
    x=1
    def f2():
        def f3():
            print(x)
        return f3
    return f2

f2=f1()

f3=f2()

f3()

'''




import time
current_user={'user':None}
def auth(engine='file'):
    def deco(func):
        def wrapper(*args,**kwargs):
            if current_user['user']:
                #已经登陆过
                res = func(*args, **kwargs)
                return res
            user=input('username>>: ').strip()
            pwd=input('password>>: ').strip()
            if engine == 'file':
                # 基于文件的认证
                if user == 'egon' and pwd == '123':
                    print('login successful')
                    # 记录用户登陆状态
                    current_user['user']=user
                    res=func(*args,**kwargs)
                    return res
                else:
                    print('user or password error')
            elif engine == 'mysql':
                print('基于mysql的认证')
            elif engine == 'ldap':
                print('基于ldap的认证')
            else:
                print('无法识别认证来源')
        return wrapper
    return deco

@auth(engine='mysql') # @deco #index=deco(index) #index=wrapper
def index():
    print('welcome to index page')
    time.sleep(1)

@auth(engine='mysql')
def home(name):
    print('welecome %s to home page' %name)
    time.sleep(0.5)

index()
# home('egon')
home('alex')