# import time
#
# def index():
#     print('welcome to index')
#     time.sleep(3)
#     return 123
#
# def home(name):
#     print('welcome %s to home page' %name)
#     time.sleep(2)
#
#
# def timmer(func):
#     #func=最原始的index
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print('run time is %s' %(stop - start))
#         return res
#     return wrapper
#
#
# index=timmer(index)
# home=timmer(home)
#
# res=index()
# home('egon')


#装饰器语法糖
# 在被装饰对象正上方，并且是单独一行写上@装饰器名

import time
def timmer(func):
    #func=最原始的index
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        stop=time.time()
        print('run time is %s' %(stop - start))
        return res
    return wrapper

# @timmer # index=timmer(index)
# def index():
#     print('welcome to index')
#     time.sleep(3)
#     return 123
# index()
#
@timmer # home=timmer(home)
def home(name):
    print('welcome %s to home page' %name)
    time.sleep(2)

# res=index()
home('egon')


# def deco(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wrapper