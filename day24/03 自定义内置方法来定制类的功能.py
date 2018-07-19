#1、__str__方法
# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     #在对象被打印时，自动触发，应该在该方法内采集与对象self有关的信息，然后拼成字符串返回
#     def __str__(self):
        # print('======>')
#         return '<name:%s age:%s>' %(self.name,self.age)
# obj=People('egon',18)
# obj1=People('alex',18)
# print(obj)  #obj.__str__()
# print(obj)  #obj.__str__()
# print(obj)  #obj.__str__()
# print(obj1)  #obj1.__str__()


# d={'x':1} #d=dict({'x':1})
# print(d)


#1、__del__析构方法
# __del__会在对象被删除之前自动触发
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.f=open('a.txt','rt',encoding='utf-8')

    def __del__(self):
        # print('run=-====>')
        # 做回收系统资源相关的事情
        self.f.close()

obj=People('egon',18)

print('主')
