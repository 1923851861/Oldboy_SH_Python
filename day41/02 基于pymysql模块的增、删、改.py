#pip3 install pymysql
import pymysql

client=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='egon123',
    database='db6',
    charset='utf8'
)

cursor=client.cursor()

# sql='insert into t1 values(3,"alex"),(4,"lxx");'
# userinfo=[
#     (3,"alex"),
#     (4,"lxx"),
#     (5,"yxx")
# ]
# for user in userinfo:
#     sql='insert into t1 values(%s,"%s");' %(user[0],user[1])
#     # print(sql)
#     cursor.execute(sql)

# sql='insert into t1 values(%s,%s);'
# cursor.executemany(sql,userinfo)

cursor.execute('delete from t1 where id=3;')

client.commit()

cursor.close()
client.close()


