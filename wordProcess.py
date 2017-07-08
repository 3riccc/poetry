#encoding:utf-8
# 在这里进行唐诗的文本处理

# 打开文件
from operator import *
f = open("quantangshi-utf8.txt")
# f = open("tangshitest.txt")

import re
# 从一行中获取句子
def getSentence(line):
	# 按照逗号和句号切割
	s = "，"
	lineArr = re.split('，|。|。 ',line)
	# 依次解码
	for index,item in enumerate(lineArr):
		lineArr[index] = lineArr[index].decode('utf8')
	# 去掉最后一项
	lineArr = lineArr[:-1]
	return lineArr

# 读取句子
allSens = []
for line in f.readlines():
	sens = getSentence(line)
	# 把句子放进数组中
	if(len(sens)!=0):
		for oneSen in sens:
			if len(oneSen) <= 7:
				allSens.append(oneSen)
# for s in allSens:
# 	print s
# print len(allSens)
# 将结果存储起来
import pickle
# 存储与读取测试——成功，本页面任务完成
# with open('allSens.pickle','wb') as f1:
#     pickle.dump(allSens,f1)
# with open('allSens.pickle','rb') as f2:
#     sss = pickle.load(f2)
# for s in sss:
# 	print s
# print len(sss)

f.close()


# 共获取464285句唐诗
