#encoding:utf-8
# 在这里进行唐诗的文本处理

# 打开文件
from operator import *
f = open("quantangshi-utf8.txt", encoding='UTF-8')
for line in f.readlines():
	# line = unicode(line, 'utf8');
	# line = line.decode('gbk').encode("utf8")
	# print line
	s = "，"
	print isinstance(line.split(s)[0].decode('utf8'),unicode)
	print line.split(s)[0].decode('utf8')
f.close()