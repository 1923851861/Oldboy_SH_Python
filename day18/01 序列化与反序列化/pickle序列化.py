import pickle

dic={'a':1,'b':2,'c':3}

# #1 序列化
# pkl=pickle.dumps(dic)
# # print(pkl,type(pkl))
#
# #2 写入文件
# with open('db.pkl','wb') as f:
#     f.write(pkl)

#1和2可以合作一步
# with open('db.pkl','wb') as f:
#     pickle.dump(dic,f)