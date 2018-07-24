#pip3 install pymysql
import pymysql

client=pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='egon123',
    database='db5',
    charset='utf8'
)

cursor=client.cursor(pymysql.cursors.DictCursor)
res=cursor.callproc('p4',(3,111)) #set @_p4_0 = 3; set @_p4_1 = 111
# print(res)

print(cursor.fetchall())

cursor.execute('select @_p4_1;')
print(cursor.fetchone())

cursor.close()
client.close()


