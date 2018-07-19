#coding:utf-8
#引用计数增加
# x=10  #10身上的引用计数加1
# y=x   #2

#引用计数减少
# x=11 #10身上的引用计数减少1
# del y #del的意思是解除绑定，10身上的引用计数减少1

#引用计数一旦为0，就是垃圾，会被python的垃圾回收机制自动回收

#python的内置功能id(),每一个变量值都有其内存地址，而id是用来反映变量值在内存中的位置的，内存地址不同id则不同
# x='info:<name:egon age:18 &/-=>'
# y='info:<name:egon age:18 &/-=>'
# print(id(x))
# print(id(y))

# x=10
# y=10
#
# print(id(x))
# print(id(y))


# x='egon'
# y='alex'
# print(id(x))
# print(id(y))