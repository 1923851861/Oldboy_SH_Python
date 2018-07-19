with open('c.txt','r+',encoding='utf-8') as f:
    f.seek(3,0)
    f.write('[a]')

# 修改文件内容的方式一：
# 思路：先将原文件内容一次性全部读入内存，然后在内存修改完毕后，再覆盖写回原文件
# 优点：在修改期间，文件内容只有一份
# 缺点：当文件过大的情况下会占用过多的内存空间

# with open('d.txt','rt',encoding='utf-8') as read_f:
#     msg=read_f.read()
#     msg=msg.replace('alex','xiang')
#     print(msg)
#
# with open('d.txt','wt',encoding='utf-8') as write_f:
#     write_f.write(msg)

# 修改文件内容的方式二：
# 思路：
# 1、以读的方式打开原文件，以写的方式打开一个新文件
# 2、从原文件中循环读取每一行内容修改后写入新文件
# 3、删除原文件，将新文件重命名为原文件的名字

# 优点：同一时刻只有一行内容存在于内存中
# 缺点：在修改期间，文件内容始终存在两份，但修改完毕后会只留一份
# import os
#
# with open('d.txt', 'rt', encoding='utf-8') as read_f, \
#         open('d.txt.swap', 'wt', encoding='utf-8') as write_f:
#     for line in read_f:
#         write_f.write(line.replace('xiang', 'ALEXSB'))
#
# os.remove('d.txt')  # 删除老文件
# os.rename('d.txt.swap', 'd.txt')
