# f.seek(offset,whence)
#offset代表文件的指针的偏移量，单位是字节bytes
#whence代表参考物，有三个取值
    #0：参照文件的开头
    #1：参照当前文件指针所在位置
    #2: 参照文件末尾
    #ps：快速移动到文件末尾f.seek(0,2)

#强调：其中whence=1和whence=2只能在b模式下使用
f=open('c.txt',mode='rt',encoding='utf-8')
f.seek(8,0)
print(f.tell()) # 每次统计都是从文件开头到当前指针所在位置
# # print(f.readline())
#
# f.close()
#
#
# f=open('c.txt',mode='rb')
# f.readline()
# f.seek(6,1)
# print(f.readline().decode('utf-8'))
# print(f.tell())
# f.close()


# f=open('c.txt',mode='rb')
# f.seek(-9,2)
# print(f.readline().decode('utf-8'))
# print(f.tell())
# f.close()



# 了解（**）
# 只有在t模式下的read(n),n代表的是字符个数，除此之外其他但凡涉及文件指针的移动都是以字节为单位的
# f=open('c.txt',mode='rt',encoding='utf-8')
# print(f.read(3))
# f.close()

# f=open('c.txt',mode='rb',)
# print(f.read(3).decode('utf-8'))
# f.close()

#
# # ab a+b r+b
# f=open('b.txt',mode='at',)
# f.truncate(9) # 参照物永远是文件开头/**个人理解，光标将位于第9个字节后，之后的内容将删除**
# f.close()



