# import os
# os.system('tasklist')

import subprocess
import time

obj=subprocess.Popen(
    'tasklist',
    shell=True, #固定格式
    stdout=subprocess.PIPE, #标准输出，与父程序的正确管道
    stderr=subprocess.PIPE #标准错误输出，与父程序的错误管道

)
# print(obj)
# stdout_res=obj.stdout.read()
# print(stdout_res.decode('gbk')) #将byte模式解码成gbk模式
# print(stdout_res)

stderr_res1=obj.stderr.read()
print(stderr_res1)  #没有结果
# stderr_res2=obj.stderr.read()
# stderr_res3=obj.stderr.read()
# print(stderr_res1.decode('gbk'))
# print(stderr_res1)
# print(stderr_res2)
# print(stderr_res3)

# import time
# time.sleep(50)