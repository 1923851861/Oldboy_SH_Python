'''
1、什么是返回值
    返回值是一个函数的处理结果，

2、为什么要有返回值
    如果我们需要在程序中拿到函数的处理结果做进一步的处理，则需要函数必须有返回值


3、函数的返回值的应用
    函数的返回值用return去定义
    格式为：
        return 值

    注意：
        1、return是一个函数结束的标志，函数内可以有多个return，
            但只要执行一次，整个函数就会结束运行

        2、return 的返回值无类型限制，即可以是任意数据类型
        3、return 的返回值无个数限制，即可以用逗号分隔开多个任意类型的值
            0个：返回None，ps：不写return默认会在函数的最后一行添加return None
            1个:返回的值就是该值本身
            多个：返回值是元组
'''

# def max2(x,y): #x=3000,y=2000
#     if x > y:
#         return x #return 3000
#     else:
#         return y #reuturn 2000
#
# res=max2(3000,2000)
#
# annual_salary=res * 12
#
# print(annual_salary)




# def foo():
#     print(1)
#     print(2)
#     print(3)
#     return [1,2,3],'a',('a','b'),{1,2}
#     print(4)
#     print(5)
#     print(6)
#
# res=foo()
# print(res)


# def bar():
#     print(1)
#     print(1)
#     print(1)
#     print(1)
#     return
#     print(2)
#     print(3)
#     print(4)
#
# res=bar()
# print(res)

