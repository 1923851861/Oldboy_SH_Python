'''
# 对象是一个高度整合的产物，整合数据与专门操作该数据的方法（绑定方法）
class Foo:
    def __init__(self,host,port,db,chartset):
        self.host=host
        self.port=port
        self.db=db
        self.charset=charset

    def exc1(self,sql):
        conn = connect(self.host, self.port, self.db, self.charset)
        conn.execute(sql)
        return xxx

    def exc2(self,proc_name)
        conn = connect(self.host, self.port, self.db, self.charsett)
        conn.call_proc(sql)
        return xxx

class Bar:
    def __init__(self,x,y,z,a,b,c):
        self.x=x
        self.y=y
        self.z=z
        self.a=a
        self.b=b
        self.c=c

    def exc3(self,xxx):
        pass

    def exc4(self,yyy)
        pass

obj1=Foo('1.1.1.1',3306,'db1','utf-8')
obj1.exc1('select * from t1')
obj1.exc1('select * from t2')
obj1.exc1('select * from t3')
obj1.exc1('select * from t4')

obj2=Foo('1.1.1.2',3306,'db1','utf-8')
obj2.exc1('select * from t4')

'''
