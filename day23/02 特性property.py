#property装饰器用于将被装饰的方法伪装成一个数据属性，在使用时可以不用加括号而直接引用
# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
# peo1=People('egon',75,1.8)
#
# peo1.height=1.85
# print(peo1.bmi)


'''
class People:
    def __init__(self,name):
        self.__name=name

    @property # 查看obj.name
    def name(self):
        return '<名字是：%s>' %self.__name

    @name.setter #修改obj.name=值
    def name(self,name):
        if type(name) is not str:
            raise TypeError('名字必须是str类型傻叉')
        self.__name=name

    @name.deleter #删除del obj.name
    def name(self):
        # raise PermissionError('不让删')
        print('不让删除傻叉')
        # del self.__name

peo1=People('egon')
# print(peo1.name)

# print(peo1.name)

# peo1.name='EGON'
# print(peo1.name)

del peo1.name

'''


class People:
    def __init__(self,name):
        self.__name=name

    def tell_name(self):
        return '<名字是：%s>' %self.__name

    def set_name(self,name):
        if type(name) is not str:
            raise TypeError('名字必须是str类型傻叉')
        self.__name=name

    def del_name(self):
        print('不让删除傻叉')

    name=property(tell_name,set_name,del_name)


peo1=People('egon')

# print(peo1.name)
peo1.name=3333
# print(peo1.name)
# del peo1.name