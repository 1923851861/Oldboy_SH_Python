'''
1 什么是多态
    多态指的是同一种事物的多种形态
        水-》冰、水蒸气、液态水
        动物-》人、狗、猪

2 为和要用多态
    多态性：
    继承同一个类的多个子类中有相同的方法名
    那么子类产生的对象就可以不用考虑具体的类型而直接调用功能

3 如何用
'''
import abc#Abstract Base Class的编写

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def speak(self):
        pass
    @abc.abstractmethod
    def eat(self):
        pass

# Animal() #强调：父类是用来指定标准的，不能被实例化

class People(Animal):
    def speak(self):
        print('say hello')

    def eat(self):
        pass

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

    def eat(self):
        pass
class Pig(Animal):
    def speak(self):
        print('哼哼哼')

    def eat(self):
        pass


#
peo1=People()
dog1=Dog()
pig1=Pig()

# People().speak()
# dog1.speak()
# pig1.speak()

def my_speak(animal):
    animal.speak()

my_speak(peo1)
# my_speak(dog1)
# my_speak(pig1)

#
# l=[1,2,3]
# s='helllo'
# t=(1,2,3)
#
# print(l.__len__())
# print(s.__len__())
# print(t.__len__())
#
# # def len(obj):
# #     return obj.__len__()
#
# print(len(l)) # l.__len__()
# print(len(s)) #s.__len__()
# print(len(t))



# python推崇的是鸭子类型，只要你叫的声音像鸭子，并且你走路的样子也像鸭子，那你就是鸭子

# class Disk:
#     def read(self):
#         print('disk read')
#
#     def write(self):
#         print('disk wirte')
#
#
# class Process:
#     def read(self):
#         print('process read')
#
#     def write(self):
#         print('process wirte')
#
#
# class File:
#     def read(self):
#         print('file read')
#
#     def write(self):
#         print('file wirte')


# obj1=Disk()
# obj2=Process()
# obj3=File()
#
#
# obj1.read()
# obj1.write()
















