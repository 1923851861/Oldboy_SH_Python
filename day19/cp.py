
import sys

# print(sys.argv)
# src_file=input('请输入源文件路径：')
src_file=sys.argv[1]
# dst_file=input('请输入目标文件路径：')
dst_file=sys.argv[2]
with open(src_file,'rb') as read_f,\
    open(dst_file,'wb') as write_f:
    for line in read_f:
        write_f.write(line)