# def bar():
#     print(1)
#     print(2)
#     print(3)
#     return [1,2,3,4],'11','我了个支'
#     print(6)
#     print(7)
#
# # res=bar()
# print(bar())

# def max2(x,y):
#     if x>y:
#         return x
#     else:
#         return y
#
# res=max2(max2(1000,2000),3000)
# print(res)

# def foo(x,y=10):
#     print('x:',x)
#     print('y:',y)
# foo(1)

# m=100
# def foo(x,y=m):
#     print('x:',x)
#     print('y:',y)
# foo(50)

# def register(name,hobby,hobbies=[]):
#     hobbies.append(hobby)
#     print('%s的爱好' %(name),end=':')
#     print(hobbies)
#
# register('aaa','play')
# register('bbb','sleep')

def register(name, hobby, hobbies=None):
    if hobbies is None:
        hobbies=[]
    hobbies.append(hobby)
    print('%s的爱好' % (name), end=':')
    print(hobbies)


register('aaa', 'play')
register('bbb', 'sleep')