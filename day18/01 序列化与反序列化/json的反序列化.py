import json

#反序列化：中间格式json-----》内存中的数据类型

# #1、从文件中读取json_str
# with open('db.json','rt',encoding='utf-8') as f:
#     json_str=f.read()
# #2、将json_str转成内存中的数据类型
# dic=json.loads(json_str)

#1和2可以合作一步
with open('db.json','rt',encoding='utf-8') as f:
    dic=json.load(f)

print(dic['sex'])