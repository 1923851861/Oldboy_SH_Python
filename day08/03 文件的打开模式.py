# 控制文件读写内容的结果有两种：t模式text,b模式bytes
# 注意：
# 1.t与b这两种模式均不能单独使用，都需要与r/w/a之一连用
# 2.默认的内容格式是t
# 3.只有文本文件才能用t模式,也只有文本文件才有字符编码的概念

# 操作文件的基础模式有三种：
# 1.r 默认的 （只读模式【默认模式，文件必须存在，不存在则抛出异常】）
# 2.w （只写模式【不可读；不存在则创建；存在则清空内容】）
# 3.a （追加写模式【不可读；不存在则创建；存在则只追加内容】）

# r:read 只读模式
# 1.只读，不写
# 2.在文件不存在时，会报错
# f = open(r'a.txt')
# # f.write(ddfdfsdff)  # 无法写入
# data = f.read()
# # print(data)
# # print(type(data))

# w:只写模式
# 1.只能写，不能读
# 2.在文件不存在时会自动创建文件，在文件存在的时候会将文件内容清空
# # f=open()
#
# # f = open(r'a.txt', mode='wt', encoding='utf-8')
# # # f.write('aaaaaa\nbbbb\nccccc\n')
# # #
# # f.close()   #回收系统资源

# a:打开以进行写入，如果存在则附加到文件的末尾
# 1.只追加写模式
# 1.只能写，不通读
# 2.在文件不存在时会创建空文件，在文件存在的时候将指针移动到文件末尾
#
# f = open(r'c.txt', mode='at', encoding='utf-8')
# f.write('1111111\n222222\n')
# f.writelines('33333\n4444\n')
#
# f.close()

# 二进制模式
# 注意：
# 1.一定不能指定字符编码，只有t模式才与字符编码有关
# 2.b是二进制模式，是一种通用的文件读取模式，因为所有的文件在硬盘中都是以二进制形式存在
# 3.将rb和wb模式结合可以实现：读写文件进行复制一份新的文件在另一个路径下，或者可以直接替换到同命名的文件再复制
# 注：复制的文件过大将无法进行操作，这是因为Python的保护机制
# f = open('1.JPG','rb')
# data=f.read()
# print(type(data))
# print(data)
# f.close()
#
# f=open(r'D:\w.jpg','wb')
# f.write(data)

# f.close()

# 循环读
# f=open('a.txt','rt',encoding='utf-8')
# for line in f:
#     print(line)
# f.close()

# f=open('1.JPG','rb')
# for line in f:
#     print(line)
# f.close()

# f=open(r'a.txt','ab')
# # f.write('你好啊'.encode('utf-8'))
# f.write('，去你妹的'.encode('utf-8'))
# f.close()

# 上下文管理
# # with open('a.txt', 'rb') as f, open('d.txt', 'wt',encoding='utf-8')as f1:  # with将完成f.close()工作，\
# #     # 无需再敲；open复制给f
# #     # 文件的操作
# #     src_data = f.read()
# #     # print(type(src_data))
# #     res = src_data.decode('utf-8')
# #     f1.write(res)

with open('a.txt', 'rb') as f, open('d.txt', 'wb')as f1:
    # src_data = f.read()
    # # print(type(src_data))
    # res = src_data.decode('utf-8')
    f1.write(f.read())