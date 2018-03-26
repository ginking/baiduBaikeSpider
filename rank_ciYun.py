# -*- coding: utf-8 -*-
import json
import datetime
import os
from pyecharts import WordCloud

def wordcloud(x,y,label):
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", x, y, word_size_range=[20, 100],shape='triangle-forward')
    wordcloud.render()
    os.system(r"render.html")

def rank(rankNum, item):
	rankList = []
	for i in range(rankNum):
		rankList.append(('name',0))
	k = 0	
	dt = datetime.datetime.now()
	with open('./info/' + dt.strftime('%Y-%m-%d') + '.json', 'r') as f:
		for line in f:
			k += 1
			try:
				data = json.loads(line)
				name = data['name']
				num = int(data[item])
				j = rankNum
				for i in range(rankNum-1,-1,-1):
					if rankList[i][1] >= num:
						break
					else:
						j = i
				if j != rankNum:
					rankList.insert(j,(name,num))
					rankList.pop()
			except:
				pass
	return rankList,k

def items():
	print('请选择统计项目\n浏览次数---1\n修改次数---2')
	num = int(input('请选择（1，2）：'))
	if num == 1:
		return 'browseNum'
	elif num == 2:
		return 'editNum'
	else:
		return None

def main():	
	item = items()
	x = []
	y = []
	if item:
		num = int(input('得到排名前n的词条，n = '))
		rankingList,totalNum = rank(num,item)
		print('共收录了%d个词条'%totalNum)
		j = 0
		for i in rankingList:
			x.append(i[0])
			y.append(i[1])
			j += 1
			print('%d.\t'%j + i[0] + '\t' + format(i[1],','))

		label = "词云"
		wordcloud(x,y,label)

	else:
		print('项目选择错误')

if __name__ == '__main__':
	main()
