# # 三元表达式
# # 条件成立时的返回值 if 条件 else 条件不成立时的返回值
#
# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
# x=10
# y=20
# res=x if x > y else y
# print(res)
#
# # 列表生成式
# l=[item**2 for item in range(1,11)]
# print(l)
#
#
# names=['alex','wxx','lxx']
#
# l=[]
# for name in names:
#     l.append(name + 'SB')
# names=l
# print(l)
#
# names=[name+'SB' for name in names]
# print(names)
#
#
# names=['alex','wxx','egon','lxx','zhangmingyan']
# l=[]
# for name in names:
#     if name != 'egon':
#         l.append(name + 'SB')
# names=l
# print(l)
# names=[name+'SB' for name in names if name != 'egon']
# print(names)
#
#
# l=[item**2 for item in range(1,5) if item > 2]
# print(l)
#
# names=['egon','alex_sb','wupeiqi','yuanhao']
# names=[name.upper() for name in names]
# print(names)
# names=['egon','alex_sb','wupeiqi','yuanhao']
#
# nums=[len(name) for name in names if not name.endswith('sb')]
# print(nums)
#
#
# 字典生成式
# s1='hello'
# l1=[1,2,3,4,5]
#
# res=zip(s1,l1)
# # print(res)
# print(list(res))
#
#
# keys=['name','age','sex']
# values=['egon',18,'male']
#
# res=zip(keys,values)
# print(list(res))
# print(list(res))
# d={}
# for k,v in zip(keys,values):
#     d[k]=v
# print(d)
#
# keys={'name':1,'age':2,'sex':3}
# a=keys
# print(a)
# keys=['name','age','sex']
# values=['egon',18,'male']
# d={k:v for k,v in zip(keys,values)}
# print(d)
#
# info={'name': 'egon', 'age': 18, 'sex': 'male'}
#
# keys=info.keys()
# print(keys)
# iter_keys=keys.__iter__()
# values=info.values()
# print(values)
#
# d={k:v for k,v in zip(keys,values)}
# print(d)
#
# s={i for i in range(10)}
# print(s,type(s))
#
#
#
# 生成器表达式
# g=(i for i in range(10))
# # print(g)
#
# print(next(g))
# print(next(g))
#
#
# nums=[11,22,33,44,55]
# print(max(nums))
#
# with open('a.txt',encoding='utf-8') as f:
#     nums=(len(line) for line in f)
#     print(max(nums))
# print(max(nums))
# print(max(nums))
#
#
#
# l=['egg%s' %i for i in range(100)]
# print(l)
#
# g=('egg%s' %i for i in range(1000000000000))
# # print(g)
# print(next(g))
# print(next(g))