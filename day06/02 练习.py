#队列：先进先出
# l=[]
# # 入队
# # l.append('王苗鲁')
# # l.append('王成龙')
# # l.append('大脑门')
# #出队
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))
#堆栈：先进后出
# l=[]
# #入栈
# l.append('王苗鲁')
# l.append('王成龙')
# l.append('大脑门')
# #出栈
#
# print(l.pop())
# print(l.pop())
# print(l.pop())




msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}

shopping_cart=[]
while True:
    for k in msg_dic:
        info='商品名：%s 价钱：%s' % (k, msg_dic[k])
        print(info.center(50,' '))
    name=input('请输入商品名>>: ').strip()
    if name not in msg_dic:
        # 输入的商品名不合法，打印提示信息并且直接进入下一次循环
        print('输了些什么玩儿。。。重输')
        continue
    # else:
    #     #输入的商品品合法，结束循环
    #     break

    while True:
        count=input('请输入购买个数：').strip()
        if count.isdigit():
            #输入个数合法
            count=int(count)
            break
        else:
            print('商品的个数必须为整数')
            # continue # 不加continue也会跳入下一次

    name,count
    for item in shopping_cart:
        # print(item)
        if name == item['name']:
            item['count']+=count
            break
    else:
        price=msg_dic[name]
        info={'name':name,'count':count,'price':price}
        shopping_cart.append(info)
    print(shopping_cart)




