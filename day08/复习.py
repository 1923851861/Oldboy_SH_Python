# 一、t模式 text
# 只读模式
# 只能读取，无法写入
# 文件存在则读取，文件不存在则报错
# f = open(r'b.txt', mode='rt')  # 打开a.txt文件，模式为rt(read,text)
# data=f.read() # 进行读取a.txt
# print(data)
# print(f.readable()) # 判断是否可读（True or False）
# print(f.readline())  # 只打印第一行字符
# print(f.readlines())  # 打印每一行字符
# print(type(data))
# f.close()

# 只写模式
# 只能进行写操作，无法进行读取
# 文件存在则覆盖文件的内容，写入新内容，文件不存在则创建文件并将新内容写入其中
# f = open(r'a.txt', mode='wt', encoding='utf-8')  # 写入中文字体时需要转码成为uft-8，不然会乱码
# f.write('1111\n2222\n3333\n4444')  # \n为换行符
# print(f.writable())  # 判断是否可读
# f.write('我了个去')  # 覆盖文件内容并将新内容写入
# f.writelines(['1\n', '2\n', '3\n', '4\n']) #功能同下方，简化
# lines=['a\nb\nc\n']
# for line in lines:
#     f.write(line)
# f.read()  # 无法进行读取操作
# f.close()

# 只追加写模式
# 只能写，不能读
# 无文件将创建空文件，有文件将指针移动到文件末尾
f = open(r'a.txt', mode='at', encoding='utf-8')
# f.write('we\nasd\nzxc')
f.writelines(['aaa\n', 'bbb\n', 'ccc'])  # 将直接追加多行字符
f.close()

#二、二进制模式
#
