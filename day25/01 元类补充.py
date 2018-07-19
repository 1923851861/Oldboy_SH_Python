class Mymeta(type):
    n=444
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self)  # self=Foo
        # obj = object.__new__(self)  # self=Foo
        self.__init__(obj, *args, **kwargs)
        return obj

class A(object):
    n=333
    # pass

class B(A):
    n=222
    # pass
class Foo(B,metaclass=Mymeta):  # Foo=Mymeta(...)
    n=111
    def __init__(self, x, y):
        self.x = x
        self.y = y


print(Foo.n)
#查找顺序：
#1、先对象层：Foo->B->A->object
#2、然后元类层：Mymeta->type


# print(type(object))

# obj=Foo(1,2)
# print(obj.__dict__)