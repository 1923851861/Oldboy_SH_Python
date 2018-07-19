'''
1、什么是函数
    函数就是具备某一特定功能的工具
2、为什么用函数
    减少重复代码
    增强程序的扩展性
    增强可读性
3、如何用函数
    1、函数的使用原则：先定义后调用（*****）
        定义阶段：只检测语法不执行代码
        调用阶段：执行函数代码
    2、定义阶段与调用阶段：
        2.1：语法 （*****）
            def func(参数1，参数2,...):
                """文档注释"""
                code1
                code2
                code3
                return 返回值
        2.2 形参与实参 （*****）
            形参本质就是变量名
            实参本质就是变量的值

            形参：
                位置形参
                    def foo(x,y):
                        pass
                默认形参
                    def foo(x,y=1):
                        pass
                *args
                    def foo(x,*args):
                        pass
                **kwargs
                    def foo(x,**kwargs):
                        pass
            实参：
                位置实参
                    foo(1,2,3,4)
                关键字实参
                    foo(x=1,y=2,z=3)
                    foo(x=1,1) # 错误
                    foo(1,x=1) #错误
                *可迭代的对象
                    foo(*'hello')
                **字典
                    foo(**{'x'：1，'y':2})

        2.3 返回值（*****）

            return是函数结束的标志，函数内可以有多个return，但只要执行一次函数就立刻结束
            并且把return后的值当作本次调用结果返回

            def foo(x,y):
                return x+y

            res=foo(1,2)

            注意:
                1、返回值可以是任意类型
                2、返回值没有个数限制
                    函数内没有return：默认返回None
                    return 值1：返回该值
                    return 值1，值2，值3：返回（值1，值2，值3）

    3、函数对象（*****）
        def foo():
            pass
        函数可以被当作数据去处理
        1、引用
            f=foo
        2、当作参数
            print(foo)
        3、当作返回值
            def bar():
                def wrapper()
                    pass
                return wrapper

            f=bar()
        4、当作容器类类型的元素
            def f1():
                pass
            def f2():
                pass

            l=[f1,f2]
            l[0]()

            func_dic={
                'f1':f1,
                'f2':f2
            }

    4、函数嵌套（*****）
        4.1 函数的嵌套调用
            def foo()
                bar()
                f1()
                f2()
            foo()
        4.2 函数的嵌套定义
            def f1():
                def f2():
                    pass
                f2()

    5、名称空间与作用域（******）
        内置名称空间
        全局名称空间
        局部名称空间
            def foo(x,y): #x=1,y=2
                pass
            foo(1,2)

        加载顺序：内置->全局-》局部
        查找名字的顺序：从当前位置往上查找
            如果当前位置在局部
            局部—》全局-》内置

        x=1
        def outter():
            def wrapper():
                print(x)
            return wrapper
        f=outter()

        def bar():
            x=111111
            f()

        全局作用域：全局存活，全局有效
            内置+全局
        局部作用域：临时存活，临时有效
            局部

        l=[]
        n=100
        def foo():
            l.append(1111)
            global n
            n=1


        def f1():
            x=1
            def f2():
                def f3():
                    nonlocal x
                    x=10

        globals()
        locals()
    6、闭包函数(****)
        x=1
        def outter():
            x=10
            def wrapper():
                print(x)
            return wrapper
        f=outter()

    7、装饰器（****）
        def deco(func):
            def wrapper(*args,**kwargs):
                res=func(*args,**kwargs)
                retutrn res
            return wrapper


        def deco1(x=1,y=2):
            def deco(func):
                def wrapper(*args,**kwargs):
                    res=func(*args,**kwargs)
                    retutrn res
                return wrapper
            return deco


        @deco
        def index():
            pass

    8  迭代器（****）
        for
        max
        min
        sorted
        filter
        map

    9  生成器（***）

    10 三元表达式、列表推导式，字典生成式，生成器表达式（*****）

        res=条件成立的结果 if 条件 else 条件成立的结果
        l=[表达式 for i in 可迭代对象 if 条件]
        g=(表达式 for i in 可迭代对象 if 条件)
        d={k:v for i in 可迭代对象 if 条件}

    11 匿名函数（*****）
        lambda 参数1,参数2:表达式

        max
        min
        sorted
        map
        filter

    12 内置函数

    13 函数递归（****）















'''


def deco1(func1): #func1=wrapper2
    def wrapper1(*args, **kwargs):
        print('第一个装饰器')
        res1 = func1(*args, **kwargs)
        return res1
    return wrapper1

def deco2(func2): #func2=最原始的index
    def wrapper2(*args, **kwargs):
        print('第二个装饰器')
        res2 = func2(*args, **kwargs)
        return res2
    return wrapper2


@deco1 #index=deco1(wrapper2)=wrapper1
@deco2 # index=deco2(index)=wrapper2
def index():
    print('from index')

index()
'''
第一个装饰器
第二个装饰器
from index
'''