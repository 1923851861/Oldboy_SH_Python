#spam.py：被导入的模块
# print('from the spam.py')
__all__=['read1','money']

money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0