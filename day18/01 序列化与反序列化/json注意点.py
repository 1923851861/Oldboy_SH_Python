# json格式不能识别单引号，全都是双引号

import json

# with open('db1.json','rt',encoding='utf-8') as f:
#     json.load(f)
#
# json.loads('{"name":"egon"}')

# with open('db.json','wt',encoding='utf-8') as f:
#     l=[1,True,None]
#     json.dump(l,f)

# 用json反序列化
# with open('db.json','rt',encoding='utf-8') as f:
#     l=json.load(f)
#     print(l)

# 用eval反列化
with open('db.json','rt',encoding='utf-8') as f:
    s=f.read() #s ='[1, true, null]'
    dic=eval(s) #eval('[1, true, null]')
    print(dic['name'])