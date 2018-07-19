'''
1 什么是调用函数
    函数名(...)即调用函数，会执行函数体代码，直到碰到return结束或者一直运行完毕所有代码

2 为何要调用函数
    用函数的功能

3、函数调用分为三种形式
    max2(1,2)
    res=max2(3000,2000) * 12
    res=max2(max2(1000,2000),3000)
'''

# def foo():
#     print(1)
#     print(2)
#     print(3)
#     return None
# res=foo()
# print(res)


def max2(x,y):
    if x > y:
        return x
    else:
        return y

#形式一：
# max2(1,2)

#形式二：
# res=max2(3000,2000) * 12
# print(res)

#形式三：
res=max2(max2(1000,2000),3000)
print(res)