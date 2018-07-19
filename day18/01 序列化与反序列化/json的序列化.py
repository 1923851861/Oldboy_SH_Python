import json

dic={'name':'egon','age':18,'sex':'male'}
#序列化：内存中的数据类型------>中间格式json

# # 1、序列化得到json_str
# json_str=json.dumps(dic)
# # 2、把json_str写入文件
# with open('db.json','wt',encoding='utf-8') as f:
#     f.write(json_str)

#1和2合为一步
with open('db.json','wt',encoding='utf-8') as f:
    json.dump(dic,f)


# print(json_str,type(json_str)) # json格式不能识别单引号，全都是双引号









