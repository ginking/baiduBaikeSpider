import pymysql
import datetime
from ciYun import wordcloud

def get_rank(items):
	rank = []
	conn = pymysql.connect(
		host='127.0.0.1',
    	user='root',
    	passwd='666666',
    	db='baidu_citiao',
    	charset='utf8')
	cursor = conn.cursor()
	dt = datetime.datetime.now()
	table_name = dt.strftime('%Y_%m_%d')
	for item in items:
		cursor.execute('select name,{item1} from {table_name} order by {item2} desc limit 30'.format(table_name=table_name,item1=item,item2=item))
		rank.append(cursor.fetchall())
	return rank 

def main():
	items = ['browseNum','editNum']
	for rank in get_rank(items):
		x = []
		y = []
		i = 0
		for r in rank:
			i += 1
			print(str(i) + '\t' + r[0] + '\t\t' + str(r[1]))
			x.append(r[0])
			y.append(r[1])
		print('')
		wordcloud(x,y)
		
	print('Done!')


if __name__ == "__main__":
	main()

