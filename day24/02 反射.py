'''
1、什么是反射
    通过字符串来操作类或者对象的属性

2、如何用
    hasattr
    getattr
    setattr
    delattr


'''

class People:
    country='China'
    def __init__(self,name):
        self.name=name

    def eat(self):
        print('%s is eating' %self.name)

peo1=People('egon')


# print(hasattr(peo1,'eat')) #peo1.eat
#
# print(getattr(peo1,'eat')) #peo1.eat
# print(getattr(peo1,'xxxxx',None))

# setattr(peo1,'age',18) #peo1.age=18
# print(peo1.age)

# print(peo1.__dict__)
# delattr(peo1,'name') #del peo1.name
# print(peo1.__dict__)

######################################################
# class Ftp:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#
#     def get(self):
#         print('GET function')
#
#     def put(self):
#         print('PUT function')
#
#     def run(self):
#         while True:
#             choice=input('>>>: ').strip()
#             # print(choice,type(choice))
#             # if hasattr(self,choice):
#             #     method=getattr(self,choice)
#             #     method()
#             # else:
#             #     print('输入的命令不存在')
#
#             method=getattr(self,choice,None)
#             if method is None:
#                 print('输入的命令不存在')
#             else:
#                 method()
#
# conn=Ftp('1.1.1.1',23)
# conn.run()



