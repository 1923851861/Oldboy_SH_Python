#作用域关系在函数定义阶段时就已经固定死了，与调用位置无关
# 即：在任意位置调用函数都需要跑到定义函数时寻找作用域关系

# def f1():
#     x=1
#     def inner():
#         print(x)
#
#     return inner
#
# func=f1()
#
# def f2():
#     x=111111
#     func()
#
# f2()

# 闭包函数：
# 闭指的是：该函数是一个内部函数
# 包指的是：指的是该函数包含对外部作用域（非全局作用域）名字的引用
# def outter():
#     x = 1
#     def inner():
#         print(x)
#
#     return inner
#
# f=outter()
#
# def f2():
#     x=1111111
#     f()
#
# f2()
#
#
# def f3():
#     x=4444444444444
#     f()
#
# f3()



# 为函数体传值的方式一：使用参数的形式
# def inner(x):
#     print(x)
#
# inner(1)
# inner(1)
# inner(1)
# 为函数体传值的方式二：包给函数
'''
def outter(x):
    # x=1
    def inner():
        print(x)
    return inner

f=outter(1)
f()
'''


# import requests
#
# def get(url):
#     response=requests.get(url)
#     if response.status_code == 200:
#         print(response.text)
#
# get('https://www.baidu.com')
# get('https://www.baidu.com')
# get('https://www.baidu.com')
#
# get('https://www.python.org')
# get('https://www.python.org')
# get('https://www.python.org')
# get('https://www.python.org')



# import requests
#
# def outter(url):
#     # url='https://www.baidu.com'
#     def get():
#         response=requests.get(url)
#         if response.status_code == 200:
#             print(response.text)
#     return get
#
# baidu=outter('https://www.baidu.com')
# python=outter('https://www.python.org')
#
#
# baidu()
# baidu()
#
# python()
# python()

