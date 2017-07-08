# encoding:utf-8
# 首先读取诗句列表
from operator import *
import pickle
with open('allSens.pickle','rb') as f2:
    allSens = pickle.load(f2)
senLen = len(allSens)

# 对某一句话分出关键词
def seperateWord(line):
	# 这行有几个字
	length = len(line)
	# 循环几次
	times = length / 2
	words = []
	for i in range(times):
		words.append(line[2*i]+line[2*i+1])
	# 最后三个字可能是一个词，也加进去
	if length > 3:
		words.append(line[-3:])
	return words


# 展示最终成果
def show(name):
	print 'name:'+name
	print 'times:'+str(finalRes[name]['times'])
	# 前面的字
	bs = ''
	for b in finalRes[name]['before']:
		bs = bs + ',' + b
	print 'before:'+bs
	# 后面的字，as是关键字，用cs替代
	cs = ''
	for c in finalRes[name]['after']:
		cs = cs + ',' + c
	print 'after:'+cs
	print "\n"
# 具体对某一行来进行关键词提炼
# line:一行的内容
# i:第几行
def dealLine(line,lineNum):
	# 把话拆分成关键词
	words = seperateWord(line)
	# 每一个词怎样处理
	for index in words:
		# 首先看这个词之前是否找过
		if index in finalRes:
			continue

		# 前面没找到过，就往后找
		# 出现次数
		times = 0
		# 这个词前面的字
		before = []
		# 这个词后面的字
		after = []

		for i in range(lineNum,senLen):
			# 如果再某句话中出现
			if index in allSens[i]:
				times += 1
				# 出现位置
				pos = allSens[i].index(index)
				# 这个词前面是什么字
				if pos > 0 :
					before.append(allSens[i][pos-1])
				else:
					# 在开头找到了，就记为下划线
					before.append("_")
				# 这个词后面是什么字
				if pos + len(index) < len(allSens[i]):
					after.append(allSens[i][pos + len(index)])
				else:
					# 在结尾找到了，后面没有词，就记为下划线
					after.append("_")
		# 出现过一次以上的词的资料计入到最终资料中
		if times != 0:
			temp = {
				'name':index,
				'times':times,
				'before':before,
				'after':after
			}
			finalRes[index] = temp
			# show(index)
			# print 'name:  '+index
			print "lines:  "+str(lineNum)

		# 单纯用于展示
		# print finalRes[index]
# 最终要保存的资料
finalRes = {}
# 开始提炼关键词
for index,line in enumerate(allSens):
	# 只处理前一千行，做一个小的样本出来
	if index > 100000 :
		continue
	# 具体处理某一行
	dealLine(line,index)
# 将结果存储起来
import pickle
# 存储与读取测试——成功，本页面任务完成
with open('words-100000.pickle','wb') as f1:
    pickle.dump(finalRes,f1)

