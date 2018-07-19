# 函数的使用必须遵循先定义,后调用的原则,
# 没有事先定义函数，而直接引用函数名，就相当于在引用一个不存在的变量名

#1、函数定义阶段:只检测函数体的语法，不执行函数体代码
# def func():
#     print('1111')
#     print('222')
#     print('333')
#
# 2、函数调用阶段:执行函数体代码
# func()
#
# 例1
# def foo():
#     print('from foo')
#     bar()
#
# foo()
#
# 例2
# def bar():
#     print('from bar')
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()
#
# # 例3
# def foo():
#     print('from foo')
#     bar()
#
# def bar():
#     print('from bar')
#
# foo()
#
#
# 例4
# def foo():
#     print('from foo')
#     bar()
#
# foo()
#
# def bar():
#     print('from bar')
