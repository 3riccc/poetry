#encoding:utf-8
# 读取上一步结果
import pickle
with open('words-100000.pickle','rb') as f1:
    words = pickle.load(f1)

# 用户输入控制
start = raw_input("请给一个开头：")
start = start.decode('utf8')
chooseType = raw_input("五言请按1，七律请按2：")
# start = '风'.decode('utf8')
# chooseType = 2

# 默认五言
lang = 5
if chooseType == str(1):
	lang = 5
elif chooseType == str(2):
	lang = 7

import random
# 按照文字提示选一个词
def chooseWordByHint(word):
	# 查看列表中有这个文字的词
	wordList = []
	for index in words:
		# 这个词中有输入的字
		if word in index:
			wordList.append({
				'name':index,
				'times':words[index]['times']
			})
	return chooseOneWord(wordList)	

# 再众多列表中，选择一个词
# 列表中每个对象都要有name和times属性
def chooseOneWord(wordList):
	# 按照概率选出这个词
	marks = [0]
	nameMarks = []
	sum = 0
	for index in wordList:
		sum += index['times']
		nameMarks.append(index['name'])
		marks.append(sum)
	# 随机数
	ran = int(random.random() * sum)
	for index,item in enumerate(marks):
		if item > ran:
			return nameMarks[index-1]

# 按照上一个词字来选下两个字
# last 上一个词
# 这个词的字数要求
def getNext(last,num):
	# 如果num是-1，那么表示不限制生成次数
	if num == -1:
		limit = False
	else:
		limit = True
	# print last
	# 如果传进来的是一个词，并且这个词被记录着
	if last in words:
		# 上一个词的after列表
		afterList = words[last]['after']
		# 哪些词的before列表含有上一个词的最后一个字？
		if num != 1:
			wordList = []
			for index in words:
				# 如果上一个字after中有下一个字，下一个字的before中有上一个字,
				if index[0] in afterList and last[-1:] in words[index]['before']:
					# 是否限制长度
					if limit:
						if len(index) == num:
							wordList.append(words[index])
					else:
						wordList.append(words[index])
			# 返回结果
			if len(wordList) > 0:
				return chooseOneWord(wordList)
		else:
			# 只要最后一个字的情况
			# 可能性有这么多
			proNum = len(words[last]['after'])
			while True:
				ran = int(random.random() * proNum)
				if words[last]['after'][ran] != "_":
					return words[last]['after'][ran]
	# 这个词不被记录着，那么就看这个词的最后一位出现在谁的before中
	else:
		wordList = []
		for index in words:
			# 这个词的before中含有上一个词的最后一个字
			if last[-1:] in words[index]['before']:
				# 限制长度
				if limit:
					if num  == len(index):
						wordList.append(words[index])
				# 不限制长度
				else:
					wordList.append(words[index])
		# 返回结果
		if len(wordList) > 0:
			return chooseOneWord(wordList)





# 打印一句话
allPeotry = []
def showSentence(sentence):
	str = ''
	for index in sentence:
		str += index
	allPeotry.append(str)
	print str

def senLength(sentence):
	str = ''
	for index in sentence:
		str += index
	return len(str)

# 生成一句诗
# start:开头的字
# last:上一行末尾的字
def oneSentence(start,last):
	sentence = []
	# 如果没有传入上一行最后一个词，说明这句话是第一句话
	if last == 0:
		# 先按照提示选一个词
		sentence.append(chooseWordByHint(start))
		# 如果是5言诗，
		if lang == 5:
			# 句子长度已经是3，那么再生成两个字就可以了
			if len(sentence) == 3:
				sentence.append(getNext(sentence[0],2))
				# return
			# 是句子长度不等于三，那么随便生成
			elif len(sentence) != 3:
				sentence.append(getNext(sentence[0],-1))
			# 如果是5言但是句子长度不够的话，那么最后加一个字
			if senLength(sentence)  == 4:
				sentence.append(getNext(sentence[1],1))
		# 如果是7言
		elif lang == 7:
			sentence.append(getNext(sentence[0],2))
			sentence.append(getNext(sentence[1],2))
			sentence.append(getNext(sentence[2],1))
	else:
		if lang == 7:
			start = last
			sentence.append(getNext(last,2))
			sentence.append(getNext(sentence[0],2))
			sentence.append(getNext(sentence[1],2))
			sentence.append(getNext(sentence[2],1))
		elif lang == 5:
			start = last
			# 先按照提示选一个词
			if senLength(sentence) == 0:
				sentence.append(chooseWordByHint(start))
			# 句子长度已经是3，那么再生成两个字就可以了
			if senLength(sentence) == 3:
				sentence.append(getNext(sentence[0],2))
				# return
			# 是句子长度不等于三，那么随便生成
			elif senLength(sentence) != 3:
				sentence.append(getNext(sentence[0],-1))
			# 如果是5言但是句子长度不够的话，那么最后加一个字
			if senLength(sentence)  == 4:
				sentence.append(getNext(sentence[1],1))
	showSentence(sentence)
oneSentence(start,0)
oneSentence(start,allPeotry[0][-1:])
oneSentence(start,allPeotry[1][-1:])
oneSentence(start,allPeotry[2][-1:])

