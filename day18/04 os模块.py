import os

# print(os.getcwd())

# print(os.listdir(r'D:\s2视频目录\day18'))
# print(os.listdir('.'))
# print(os.listdir('..'))

# os.chdir(r'D:\s2视频目录\day08')
# print(os.getcwd())

# print(os.listdir(r'D:\s2视频目录\day08'))
# print(os.listdir(r'.'))

# os.mkdir(r'a')
# os.mkdir(r'a/b')
# os.mkdir(r'a/b/c')

# os.makedirs(r'a\b\c\d\e\f')
# os.rmdir(r'a\b\c\d\e\f')
# os.removedirs(r'a\b\c\d\e\f')

# obj=os.stat(r'D:\s2视频目录\day18\run.py')
# print(obj)

# print(os.sep)
# print(os.linesep)
# print(os.pathsep)

# import time,os
# print(os.getpid())
# time.sleep(500)

# res=os.system('taskliasdfst')
# print('结果是：',res)


# import json
#
# # 当程序所有的文件都需要引用一个变量时，则需要将该变量加入环境变量中
# os.environ['x']=json.dumps(['a','b','c'])
# print(json.loads(os.environ['x'])[0])






# print(os.path.split(r'D:\s2视频目录\day18\03 random模块.py'))
# print(os.path.dirname(r'D:\s2视频目录\day18\03 random模块.py'))
# print(os.path.basename(r'D:\s2视频目录\day18\03 random模块.py'))




# print(os.path.isabs(r'C:\a\b.txt'))
# print(os.path.isabs(r'a\b.txt'))

# print(os.path.isabs('/a/b/c.txt'))
# print(os.path.isabs('a/b/c.txt'))

# print(os.path.join('C:\\','a','D:\\','b','F:\\','c.txt'))

print(os.path.getsize(r'D:\s2视频目录\day18\02 时间模块.py')) #字节