# names=['egon','asb','wsb','lsb','csb']

# n=0
# while n < len(names):
#     print(names[n])
#     n+=1


# names=['egon','asb','wsb','lsb','csb']
# info={'name':'egon','age':18,'sex':'male'}
#
# # for k in info: #x=''age'
# #     print(k,info[k])
#
# for item in names:
#     print(item)


# for i in range(1,10):
#     print(i)

# for i in range(10): #默认的起始位置是0
#     print(i)

# for i in range(1,10,2): #1 3  5  7  9
#     print(i)

# names=['egon','asb','wsb','lsb','csb']
# for i in range(len(names)):
#     print(i,names[i])

# for i in range(5):
#     print('========>第一层: %s<=========' %i)
#     for j in range(3):
#         print('          第二层: %s' %j)


#for+break
# names=['asb','wsb','egon','lsb','csb']
# for n in names:
#     if n == 'egon':
#         break
#     print(n)

#for+continue
# names=['asb','wsb','egon','lsb','csb']
# for n in names:
#     if n == 'egon':
#         continue
#     print(n)


#for+else
names=['asb','wsb','egon','lsb','csb']
for n in names:
    # if n == 'egon':
    #     break
    print(n)
else:
    print('=====>')