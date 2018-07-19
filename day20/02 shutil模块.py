import shutil

# with open('old.xml','r') as read_f,open('new.xml', 'w') as write_f:
#     shutil.copyfileobj(read_f,write_f)
#


# shutil.make_archive("data_bak", 'gztar', root_dir='D:\SH_fullstack_s2\day04')

import tarfile
t=tarfile.open('data_bak.tar.gz','r')
t.extractall('D:\SH_fullstack_s2\day20\dir')
t.close()