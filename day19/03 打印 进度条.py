'''

[#                  ]
[##                 ]
[###                ]
[####               ]
[#####              ]

'''
# print('[%-50s]' %'#')
# print('[%-50s]' %'##')
# print('[%-50s]' %'###')
# print('[%-50s]' %'####')
# print('[%-50s]' %'#####')

# print('%s%%' %50)

# 1、控制打印进度条的宽度
# res='[%%-%ds]' %50
# print(res %'#')
# print(res %'##')
# print(res %'###')
# print(res %'####')
# print(res %'#####')

#2、不换行+跳回行首打印
# import time
# print(('\r[%%-%ds]' %50) %'#',end='')
# time.sleep(0.5)
# print(('\r[%%-%ds]' %50) %'##',end='')
# time.sleep(0.5)
# print(('\r[%%-%ds]' %50) %'###',end='')
# time.sleep(0.5)
# print(('\r[%%-%ds]' %50) %'####',end='')
# time.sleep(0.5)
# print(('\r[%%-%ds]' %50) %'#####',end='')


# 作业：打印进度条
import time

def make_progress(percent,width=50):
    if percent > 1:percent=1
    show_str=('[%%-%ds]' % width) % (int(percent * width) * '#')
    print('\r%s %s%%' %(show_str,int(percent * 100)),end='')

total_size=102400
recv_size=0
while recv_size < total_size:
    time.sleep(0.1) # 模拟经过了0.5s的网络延迟下载了1024个字节
    recv_size+=1024
    # 调用打印进度条的功能去打印进度条
    percent=recv_size / total_size
    make_progress(percent)






