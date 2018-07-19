import pickle


# # #1、从文件中读取pickle格式
# with open('db.pkl','rb') as f:
#     pkl=f.read()
# #2、将json_str转成内存中的数据类型
# dic=pickle.loads(pkl)
# print(dic['a'])

#1和2可以合作一步
# with open('db.pkl','rb') as f:
#     dic=pickle.load(f)
#
# print(dic['a'])


import json,pickle

s={1,2,3}
# json.dumps(s)
pickle.dumps(s)