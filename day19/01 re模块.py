"""
1、什么是正则
    正则就是用一系列具有特殊含义的字符组成一套规则，该规则用来描述具有某一特征的字符串，
    正则就是用来去一个大的字符串中匹配出符合规则的子字符串

2、为什么要用正则
    1、用户注册
    2、爬虫程序

3、如何用正则


"""
import re

# print(re.findall('\w','hello 123_ */-='))
# print(re.findall('\W','hello 123_ */-='))

# print(re.findall('\s','hell\no 12\t3_ */-='))
# print(re.findall('\S','hell\no 12\t3_ */-='))

# print(re.findall('\d','hell\no 12\t3_ */-='))
# print(re.findall('\D','hell\no 12\t3_ */-='))

# print(re.findall('\n','hell\no 12\t3_ */-='))
# print(re.findall('\t','hell\no 12\t3_ */-='))
# print(re.findall('l','hell\no 12\t3_ */-='))


# print(re.findall('egon','my name is egon,egon is beautiful'))
#                                                      egon
# print(re.findall('^egon','egon my name is egon,egon is beautiful'))
# print(re.findall('egon$','egon my name is egon,egon is beautifulegon1'))
#                                                                egon


# 重复匹配
# .:匹配换行符以外的任意一个字符
# print(re.findall('a.c','abc a1c aac asd aaaaac a*c a+c abasd')) #['abc','a1c','aac','aac','a*c','a+c']
#                                                        a.c
# print(re.findall('a.c','abc a1c aac a\nc asd aaaaac a*c a+c abasd',re.DOTALL))

# []:匹配一个字符,该字符属于中括号内指定的字符
# print(re.findall('a..c','abc a1 c aac asd aaaaac a *c a+c abasd ='))
# print(re.findall('a.c','abc a1 c aac aAc aBc asd aaaaac a-c a/c a *c a+c abasd = a1c a2c'))
# print(re.findall('a[a-z]c','abc a1 c aac aAc aBc asd aaaaac a-c a/c a *c a+c abasd = a1c a2c'))
# print(re.findall('a[^A-Z]c','abc a1 c aac aAc aBc asd aaaaac a-c a/c a *c a+c abasd = a1c a2c'))
# print(re.findall('a[-+*/]c','abc a1 c aac aAc aBc asd aaaaac a-c a/c a *c a+c abasd = a1c a2c'))
# print(re.findall('a[a-z][a-z]c','abc a1 c aac aAc aBc asd aaaaac a-c a/c a *c a+c abasd = a1c a2c'))
# print(re.findall('a[^a-z]c','abc a1 c aac aAc aBc asd aaaaac a-c a/c a *c a+c abasd = a1c a2c'))


# *: 必须与其他字符连用，代表左侧的字符出现0次或者无穷次
# print(re.findall('ab*','a ab abbb abbbb a1bbbb a-123'))
#                                              ab*
#['a','ab','abbb','abbbb','a','a']
# print(re.findall('ab{0,}','a ab abbb abbbb a1bbbb a-123'))



# ?： 必须与其他字符连用,代表左侧的字符出现0次或者1次
# print(re.findall('ab?','a ab abbb abbbb a1bbbb a-123'))
#                                              ab?
#['a','ab','ab','ab','a','a']
# print(re.findall('ab{0,1}','a ab abbb abbbb a1bbbb a-123'))



# +： 必须与其他字符连用,代表左侧的字符出现1次或者无穷次
# print(re.findall('ab+','a ab abbb abbbb a1bbbb a-123'))
#                                              ab+
# ['ab','abbb','abbbb']
# print(re.findall('ab{1,}','a ab abbb abbbb a1bbbb a-123'))


# {n,m}： 必须与其他字符连用
# print(re.findall('ab{1,3}','a ab abbb abbbb a1bbbb a-123'))
#                                                  ab{1,3}
# ['ab','abbb','abbb']


# .*：贪婪匹配
# print(re.findall('a.*c','ab123adfc1134124123adasfc123123'))

# .*?:非贪婪匹配
# print(re.findall('a.*?c','ab123adfc1134124123adasfc123123'))
#                                            a.*?c


#():分组
# print(re.findall('expression="(.*?)"','expression="1+2+3/4*5" egon="beautiful"'))
#                                       expression=".*?"


# print(re.findall('href="(.*?)"','<p>段落</p><a href="https://www.sb.com">点我啊</a><h1>标题</h1><a href="https://www.sb.com">点我啊</a>'))



#|：
# print(re.findall('a|b','ab123abasdfaf'))
#                        a|b

# print(re.findall('compan(?:ies|y)','Too many companies have gone bankrupt, and the next one is my company'))

#companies   company



# print(re.findall(r'a\\c','a\c a1c aAc aac'))
# print(re.findall('a\\\\c','a\c a1c aAc aac'))

# print(re.findall('ale(x)','alex is SB,alex is bigSB'))
# print(re.search('alex','alex is SB,alex is bigSB'))
# print(re.search('ale(x)','alex is SB,alex is bigSB').group())
# print(re.search('abcdefg','alex is SB,alex is bigSB'))

# print(re.search('^alex','123alex is SB,alex is bigSB'))
# print(re.match('alex','123alex is SB,alex is bigSB'))

# l='egon:18:male'.split(':')
# print(l)
# l1=re.split('[ |:/-]','a-b/c egon:18:male xxx|qqq')#-因为有其特殊作用，只能放在首位或者末尾才能生效
# print(l1)

# print(re.sub('[a-z]+xx','yxp','lxx is good,sb is lllxx wxx is good cxx is good'))
#                                                   [a-z]+xx

# pattern=re.compile('alex')
# print(pattern.findall('alex is SB,alex is bigSB'))
# print(pattern.search('alex is SB,alex is bigSB'))
