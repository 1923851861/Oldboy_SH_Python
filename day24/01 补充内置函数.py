class Foo:
    pass

obj=Foo()

print(isinstance(obj,Foo))

# 在python3中统一类与类型的概念
# d={'x':1} #d=dict({'x':1} #)
#
# print(type(d) is dict)
# print(isinstance(d,dict))

# issubclass()


# class Parent:
#     pass
#
# class Sub(Parent):
#     pass
#
# print(issubclass(Sub,Parent))
# print(issubclass(Parent,object))