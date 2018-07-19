#函数的嵌套定义
def f1():
    def f2():
        print('from f2')
    f2()
f1()




# from math import pi
#
# def circle(radius,action='area'): #radius=10
#     def area():
#         return pi * (radius ** 2)
#
#     def perimeter():
#         return 2 * pi * radius
#
#     if action == 'area':
#         return area()
#     elif action == 'perimeter':
#         return perimeter()
#
# print(circle(10))
# print(circle(10,action='perimeter'))





#函数的嵌套调用
# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def max4(a,b,c,d):
#     res1=max2(a,b)
#     res2=max2(res1,c)
#     res3=max2(res2,d)
#     return res3
# #
# print(max4(1,2,3,4))