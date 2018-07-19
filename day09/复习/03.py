# with open('a.txt','rt',encoding='utf-8') as read_f:
#     msg=read_f.read()
#     msg1=msg.replace('一','二')
#     print(msg1)
#
# with open('a.txt','w',encoding='utf-8') as write_f:
#     write_f.write(msg1)

# with open('a.txt','r',encoding='utf-8') as read_f:
#     msg=read_f.read()
#     msg1=msg.replace('三','3')
#
# with open('a.txt','w',encoding='utf-8') as write_f:
#     write_f.write(msg1)

import os

with open('a.txt', 'r', encoding='utf-8')as read_f, \
        open('a.txt.aaa', 'w', encoding='utf-8')as write_f:
    read_f = read_f.read()
    write_f.write(read_f.replace('二', '十'))

os.remove('a.txt')  # 删除原文件
os.rename('a.txt.aaa', 'a.txt')  # 重命名新文件
