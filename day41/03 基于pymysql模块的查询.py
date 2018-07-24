# #pip3 install pymysql
# import pymysql
#
# client=pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='egon123',
#     database='db6',
#     charset='utf8'
# )
#
# cursor=client.cursor()
# #查询
# inp_user=input('输入账号名: ').strip()
# inp_pwd=input('输入密码: ').strip()
#
# # sql='select id from user where name = "%s" and pwd = password("%s");' %(inp_user,inp_pwd)
# sql='select id from user where name = "%s" and pwd = "%s";' %(inp_user,inp_pwd)
# print(sql)
# rows=cursor.execute(sql)
# if rows:
#     print('\033[45m登陆成功\033[0m')
# else:
#     print('\033[46m用户名或密码错误\033[0m')
#
# cursor.close()
# client.close()
#
#


# 解决 sql注入问题
#pip3 install pymysql
# import pymysql
#
# client=pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='egon123',
#     database='db6',
#     charset='utf8'
# )
#
# cursor=client.cursor()
# #查询
# inp_user=input('输入账号名: ').strip()
# inp_pwd=input('输入密码: ').strip()
#
# sql='select id from user where name = %s and pwd = %s;'
# rows=cursor.execute(sql,(inp_user,inp_pwd))
# if rows:
#     print('\033[45m登陆成功\033[0m')
# else:
#     print('\033[46m用户名或密码错误\033[0m')
#
# cursor.close()
# client.close()

# 提交查询语句并且拿到查询结果
import pymysql

client=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='egon123',
    database='db6',
    charset='utf8'
)

cursor=client.cursor(pymysql.cursors.DictCursor)
#查询

sql='select * from user where id > 3'
rows=cursor.execute(sql)
# print(rows)
# print(cursor.fetchall())
# print(cursor.fetchall())

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# print(cursor.fetchmany(2))
# print(cursor.fetchone())




# print(cursor.fetchall())
# # cursor.scroll(0,mode='absolute') # 绝对位置移动
# # cursor.scroll(1,mode='absolute') # 绝对位置移动
# print(cursor.fetchall())


# print(cursor.fetchone())
# cursor.scroll(2,mode='relative') # 相对当前位置移动
# print(cursor.fetchone())

cursor.close()
client.close()

