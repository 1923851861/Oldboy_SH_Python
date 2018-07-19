import shelve

# dic1={'pwd':'alex3714','age':18,'sex':'male'}
# dic2={'pwd':'alex3715','age':73,'sex':'male'}

d=shelve.open('db.txt',writeback=True)#writeback值为True可将更改内容覆盖回原文件
# # d['egon']=dic1
# # d['alex']=dic2
# d['egon']['age']=19
print(d['egon'])
d.close()