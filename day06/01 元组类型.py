# 一：基本使用
# 1 用途：元组是不可变的列表，能存多个值，但多个值只有取的需求，而没有改的需求，那么用元组合最合理
#
# 2 定义方式:在()内用逗号分割开，可以存放任意类型的值
# names=('alex','egon','wxx') #names=tuple(('alex','egon','wxx'))
# print(type(names))
# 强调: 当元组内只有一个元素时，务必记住加一个逗号
# x=('egon',)
# print(type(x))

# 3 常用操作+内置的方法
# 1、按索引取值(正向取+反向取)：只能取
# names=('alex','egon','wxx')
# names[0]='sb'


# 2、切片(顾头不顾尾，步长)
# names=('alex','egon','wxx','lxx','cxxx')
# print(names[1:3]
# )

# 3、长度
# names=('alex','egon','wxx','lxx','cxxx')
# print(len(names))
# 4、成员运算in和not in
# names=('alex','egon','wxx','lxx','cxxx')
# print('alex' in names)

# 5、循环
# names=('alex','egon','wxx','lxx','cxxx')
# for item in names:
#     print(item)


# #二：该类型总结
# 1 存一个值or存多个值
#     可以存多个值，值都可以是任意数据类型
#
# 2 有序or无序
# 有序
# 3 可变or不可变
# 不可变

# names=('alex','egon','wxx','lxx','cxxx','lxx')
# del names[0]
# names[0]='sb'
# print(names.count('lxx'))
# print(names.index('wxx',0,3))

# names=('alex','egon','wxx','lxx','cxxx','lxx')
# names=1

# l=[1,243,3]
# l=3333
# l=['a','b','c']
# print(id(l[0]))
# l[0]='A'
# print(id(l[0]))

# names=('a','b','c')

# 列表可变的底层原理：
# 指的是索引所对应的值的内存地址是可以改变的

# 元组不可变的底层原理：
# 指的是索引所对应的值的内存地址是不可以改变的
# 或者反过来说，只要索引对应值的内存地址没有改变，那么元组始终是没有改变的
#
# t1 = (['a', 'b', 'c'], 'wc', 'office')
#
# print(id(t1[0]))
# print(id(t1[1]))
# print(id(t1[2]))
#
# t1[0][0] = 'AAAA'
# print(t1)
#
# print(id(t1[0]))
