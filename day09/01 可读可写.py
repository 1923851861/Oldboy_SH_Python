#r+t:可读、可写

#w+t:可写、可读
# with open('b.txt','w+t',encoding='utf-8') as f:
#     print(f.readable())
#     print(f.writable())
#a+t:可追加写、可读

#r+b
#w+b
#a+b

# with open('b.txt',mode='rb') as f:
#     data=f.read()
#     print(data.decode('utf-8'))

# with open('b.txt',mode='rt',encoding='utf-8') as f:
#     data=f.read()
#     print(data)

# with open('a.txt',mode='r+',encoding='utf-8') as f:
#     print(f.readline())
#     print(f.readline())
#     f.write('小红帽')



