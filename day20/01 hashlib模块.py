'''
1 什么是hash
    hash是一种算法，该算法接受传入的内容，经过运算得到一串hash值
    如果把hash算法比喻为一座工厂
    那传给hash算法的内容就是原材料
    生成的hash值就是生产出的产品

2、为何要用hash算法
    hash值/产品有三大特性：
        1、只要传入的内容一样，得到的hash值必然一样
        2、只要我们使用的hash算法固定，无论传入的内容有多大，
            得到的hash值的长度是固定的
        3、不可以用hash值逆推出原来的内容

        基于1和2可以在下载文件时做文件一致性校验
        基于1和3可以对密码进行加密

3、如何用
'''
import hashlib

# #1、造出hash工厂
# m=hashlib.md5()
#
# #2、运送原材料
# m.update('你好啊美丽的'.encode('utf-8'))
# m.update('张铭言'.encode('utf-8'))
#
# #3、产出hash值
# print(m.hexdigest()) #66bcb9758826f562ae8cb70d277a4be9




# #1、造出hash工厂
# m=hashlib.md5('你'.encode('utf-8'))
#
# #2、运送原材料
# m.update('好啊美丽的张铭言'.encode('utf-8'))
#
# #3、产出hash值
# print(m.hexdigest()) #66bcb9758826f562ae8cb70d277a4be9



# 应用一：文件一致性校验
# #1、造出hash工厂
# m=hashlib.sha512('你'.encode('utf-8'))
#
# #2、运送原材料
# m.update('好啊美sadfsadf丽asdfsafdasdasdfsafsdafasdfasdfsadfsadfsadfsadfasdff的张铭言'.encode('utf-8'))
#
#
# #3、产出hash值
# print(m.hexdigest()) #2ff39b418bfc084c8f9a237d11b9da6d5c6c0fb6bebcde2ba43a433dc823966c


# #1、造出hash工厂
# m=hashlib.md5()
#
# #2、运送原材料
# with open(r'E:\01.mp4','rb') as f:
#     for line in f:
#         m.update(line)
# #3、产出hash值
# print(m.hexdigest()) #1273d366d2fe2dc57645cc1031414a05
# #                     1273d366d2fe2dc57645cc1031414a05



# 应用二：对明文密码进行加密
# password=input('>>>: ')
#
# m=hashlib.md5()
# m.update('天王盖地虎'.encode('utf-8')) #在用户输入明文密码进行加密基础上增加字符串实现加密复杂性,明文密码更安全
# m.update(password.encode('utf-8'))
# print(m.hexdigest()) #95bd6eafefdf51d8b153785f3fb6263d
#
#
#
# import hmac
#
# m=hmac.new('小鸡炖蘑菇'.encode('utf-8'))
# m.update('hello'.encode('utf-8'))
# print(m.hexdigest())






