names=['lxx','alex','wupeiqi','yuanhao',4,5]
# print(names[-3])
# print(names[1:4:2])
# print(len(names))

# if 'alex' in names:
#     i=names.index('alex')
#     names[i]='alex_SB'
# if 'egon' in names:
#     names.remove('egon')
#
# print(names)

# 二、有如下列表，请采用两种方式取出列表中的值
my_girl_friends = ['alex', 'wupeiqi', 'yuanhao', 4, 5]
# 方式一：依赖索引，请写出while循环与for循环两种实现方式
# count=0
# while count < len(my_girl_friends):
#     print(my_girl_friends[count])
#     count+=1

# for i in range(len(my_girl_friends)):
#     print(my_girl_friends[i])

# 方式二：不依赖索引
# for item in my_girl_friends:
#     print(item)

# 三、说明白，数字、字符串、列表之间能否比较大小，如果能，请说明白各种情况下的比较方式

# if 'egon'  not in names:
#     names.append('egon')
# print(names)

#	六、交叉赋值
# y=10
# x=11
# x,y=y,x
# 七、变量的解压
# l=[1,2,3]
# x=l[0]
# y=l[1]
# z=l[2]
# x,y,z=l




#十一：
# students=[
# 		{'name':'alex_sb','age':18},
# 		{'name':'egon','age':18},
# 		{'name':'wupeiqi_sb','age':18},
# 	]
#
# for info in students:
#     if 'sb' in info['name']:
#         print(info['name'],info['age'])
# print('sb' in students[0]['name'])
# print('sb' in students[1]['name'])
# print('sb' in students[2]['name'])
# print('sb' in students[3]['name'])
# print('sb' in students[4 ]['name'])

# 十三
# user='egon-18-male-play'
# l=user.split('-')
# print(l[2])


# 十六
# data=['alex',49,[1900,3,18]]
# x,y,z=data
# print(x,y,z)

#十七：

'''
1*1=1
2*1=2 2*2=4
3*1=3 3*2=6 3*3=9
4*1=4 4*2=8 4*3=12 4*4=16
...
9*1 ....             9*9=81
'''
# for i in range(1,10): #i=2
#     for j in range(1,i+1): #1 2    j=2
#         print('%s*%s=%s' %(i,j,i*j),end=' ') #'2*1=2'  '2*2=4'
#     print()

'''

'''
max_level=50
for level in range(1, max_level + 1):  # 控制的层数
    # level的值是第几层 #level=

    # 第一件事：重复地打印空格
    for x in range(max_level - level):
        print(' ', end='')

    # 第二件事：重复地打印*
    for y in range(2 * level - 1):
        print('*', end='')

    # 第三件事：打印一个换行
    print()




# print('egon',end='')
# print('egon',end='')
# print('egon',end='')