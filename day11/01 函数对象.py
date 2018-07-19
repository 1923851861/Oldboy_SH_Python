#函数是第一类对象的含义是函数可以被当作数据处理


#
def func(): #func=<function func at 0x0584BA50>
    print('from func')

# print(func)


# x='hello'
#1、引用
# y=x
# f=func
# print(f)
# f()


#2、当作参数传给一个函数
# len(x)
# def foo(m):
#     # print(m)
#     m()
#
# foo(func)


#3、可以当作函数的返回值
# def foo(x): #x=func
#     return x #return func
#
# res=foo(func)
# # print(res)
# res()

#4、可以当作容器类型的元素
# l=[x,]

# l=[func,]
# print(l)
#
# l[0]()

#
#
# def pay():
#     print('支付。。。')
#
# def withdraw():
#     print('取款。。。')
#
# def transfer():
#     print('转账。。。')
#
# def check_balance():
#     print('查看余额。。。')
#
#
# def shopping():
#     print('购物。。。')
#
# func_dic={
#     '1':pay,
#     '2':withdraw,
#     '3':transfer,
#     '4':check_balance,
#     '6':shopping
# }
#
# while True:
#     msg="""
#     1 支付
#     2 取款
#     3 转账
#     4 查看余额
#     5 退出
#     6 购物
#     """
#     print(msg)
#     choice=input('>>: ').strip()
#     if choice == '5':break
#     if choice not in func_dic:
#         print('输入的指令不存在傻叉')
#         continue
#     func_dic[choice]()




# def pay():
#     print('支付...')
# def withdraw():
#     print('取款...')
# def transfer():
#     print('转账...')
# def check_balance():
#     print('查看余额...')
# def shopping():
#     print('购物')
#
# func_dict={
#     '1':pay,
#     '2':withdraw,
#     '3':transfer,
#     '4':check_balance,
#     '5':shopping
#
#
# }
#
# while True:
#
#     msg="""
#     1.支付
#     2.取款
#     3.转账
#     4.查看余额
#     5.购物
#     6.退出
#
#
#     """
#     print(msg)
#     choice=input('请输入你的操作>>:').strip()
#     if choice=='6':
#         print('再见,穷B')
#         break
#     if choice not in func_dict:
#         print('输入有误，请确认')
#         continue
#
#     func_dict[choice]()
