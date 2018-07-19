import xml.etree.ElementTree as ET

tree = ET.parse("a.xml")
root = tree.getroot()

# 对于任何标签都有三个特征：标签名、标签属性、标签的文本内容
# print(root.tag)
# print(root.attrib)
# print(root.text)

# print(list(root.iter('year'))) #全文搜索,找到所有
# for year in root.iter('year'):
#     print(year.tag)
#     print(year.attrib)
#     print(year.text)
#     print('='*100)


# print(root.find('country').attrib) #在root的子节点找，只找一个
# print([country.attrib for country in root.findall('country')]) #在root的子节点找，找所有


# 1、查
#遍历整个文档
# for country in root:
#     print('============>国家 %s' %country.attrib)
#     for item in country:
#         print(item.tag)
#         print(item.attrib)
#         print(item.text)

#2、改
# for year in root.iter('year'):
#     print(year.tag)
#     year.attrib={'updated':'yes'}
#     year.text=str(int(year.text)+1)
#
# tree.write('a.xml')

#3、增
# for country in root:
#     rank=country.find('rank')
#     if int(rank.text) > 50:
#         # print('符号条的国家',country.attrib)
#         tag=ET.Element('egon')
#         tag.attrib={'updated':'yes'}
#         tag.text='NB'
#         country.append(tag)
#
# tree.write('a.xml')
#4、删

for country in root:
    tag=country.find('egon')
    # print(tag,bool(tag))
    if tag is not None:
        print('====>')
        country.remove(tag)
tree.write('a.xml')







