#一：基本使用
# 1 用途：用来存多个值，但每一个值都有一个key与之对应，key对值有描述性的功能
#        当存储多个值表示的不同的状态时，
#
# 2 定义方式:{}内用逗号分隔开多个元素，每一个元素都是key：value的形式
#value可以是任意数据类型，但是key必须为不可变类型，key通常应该是字符串类型，
# d={'x':1,'y':2} #d=dict({'x':1,'y':2})
# d=dict(a=1,b=2,c=3)
# print(d)


# dic={1:'a',0:'b',1.1:'c',(1,2,3):'d'}
# print(dic[1])
# print(dic[0])
# print(dic[1.1])
# print(dic[(1,2,3)])
# dic={[1,2,3]:'a'}
# dic={{'x':1}:'a'}

#
# 3 常用操作+内置的方法
#优先掌握的操作：
#1、按key存取值：可存可取
# d={'x':1,'y':2}
# d['x']=100
# print(d)
# d['z']=3
# print(d)

# l=['a','b']
# l[2]='c'

#2、长度len
# d={'x':1,'y':2}
# print(len(d))
#3、成员运算in和not in
# d={'x':1,'y':2}
# print('x' in d)

#4、删除
d={'x':1,'y':2}
# del d['x']
# print(d)
# res=d.pop('y')
# print(d)
# print(res)

# res=d.popitem()
# print(d)
# print(res)

# d={'a':1,'b':2,'c':3,'d':4}
# for k in d:
#     print(k)

# l=[1,2,3]
# del l[1]
# print(l)

#5、键keys()，值values()，键值对items()
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
# names=[]
# for k in msg_dic:
#     names.append(k)
# print(names)
# values=[]
# for k in msg_dic:
#     values.append(msg_dic[k])
# print(values)

# keys=msg_dic.keys()
# print(keys)
# for k in keys:
#     print(k)=
# l=list(keys)
# print(l)

# vals=msg_dic.values()
# print(vals)
# print(list(vals))

# print(msg_dic.items())
# print(list(msg_dic.items()))
#6、循环
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
# 只取key
# for k in msg_dic:
#     print(k,msg_dic[k])

# for k in msg_dic.keys():
#     print(k,msg_dic[k])

# 只取value
# for v in msg_dic.values():
#     print(v)

#取key和value
# for k,v in msg_dic.items(): #k,v=('apple', 10)
#     print(k,v)

# 需要掌握的内置方法（****）
# d={'x':1,'y':2,'z':3}
# v=d.get('xxxx')
# print(v)
# print(d['xxxxxxx'])

# d={'x':1,'y':2,'z':3}
# d1={'a':1,'x':1111111}
# d.update(d1)
# print(d)

# l=['name','age','sex']
# d={}
# for k in l:
#     d[k]=None
# d=dict.fromkeys(l,None)
# print(d)


# info.setdefault
info={'name':'egon','age':18,'sex':'male'}

# 如果字典中有setdefault指定的key，那么不改该key对应的值，返回原的value
# res=info.setdefault('name','EGON_NB')
# print(info)
# print(res)

# 如果字典中没有setdefault指定的key，那么增加一个key:value,返回新的value
# info.setdefault('height',1.80)
# print(info)

# info={'age':18,'sex':'male'}
# v=info.setdefault('name','浩哥')
# print(v)




s='hello alex alex say hello sb sb'
l=s.split()
# print(l)
d={}
# for word in l: #word=  'hello'
#     if word not in d:
#         d[word]=1 #{'hello':2, 'alex':2,'say':1}
#     else:
#         d[word]+=1
# print(d)

s='hello alex alex say hello sb sb'
l=s.split()
print(l)
d={}

# d={'hello':2,'alex':2}
for word in l: #word='alex'
    # d[word]=l.count(word) #d['alex']=2
    d.setdefault(word,l.count(word))

print(d)











# #二：该类型总结
# 1 存一个值or存多个值
#     可以存多个值，值都可以是任意类型，而key必须是不可变类型，通常应该是不可变类型中字符串类型
#
# 2 有序or无序
# 无序
#
# 3 可变or不可变

d={'x':1,'y':2}
# print(id(d))
# d['x']=1111
# print(id(d))

d=123