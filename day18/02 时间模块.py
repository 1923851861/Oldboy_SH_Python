import time
# 时间分为三种格式
#1、时间戳
# start= time.time()
# time.sleep(3)
# stop= time.time()
# print(stop - start)

#2、格式化的字符串形式
# print(time.strftime('%Y-%m-%d %X'))
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))

#3、 结构化的时间/时间对象
# t1=time.localtime()
# print(t1)
# print(type(t1.tm_min))
# print(t1.tm_mday)

# t2=time.gmtime()
# print(t1)
# print(t2)

# 时间转换
# print(time.localtime(123123123))
# print(time.gmtime(123123123))

# print(time.mktime(time.localtime()))

# print(time.strftime('%Y',time.localtime()))
# print(time.strptime('2011-03-07','%Y-%d-%m'))


# print(time.asctime())
# print(time.ctime())
# print(time.strftime('%a %b %d %H:%M:%S %Y'))

# print(time.asctime(time.localtime()))
# print(time.ctime(123123123))

# print(time.strftime('%Y-%m-%d %X'))




# 获取格式化字符串形式的时间麻烦
# 时间戳与格式化时间之间的转换麻烦
# 获取之前或者未来的时间麻烦
import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.fromtimestamp(1231233213))

# print(datetime.datetime.now() + datetime.timedelta(days=3))
# print(datetime.datetime.now() + datetime.timedelta(days=-3))


s=datetime.datetime.now()
print(s.replace(year=2020))

