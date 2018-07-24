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

sql='insert into t1 values(1,"egon");'
try:
    res=cursor.execute(sql)
    print(res)
    # cursor.execute(sql)
    # cursor.execute(sql)
    # cursor.execute(sql)
    client.commit()
except Exception:
    client.rollback()

cursor.close()
client.close()


