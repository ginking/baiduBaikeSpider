import os
from pyecharts import WordCloud

def wordcloud(x,y):
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", x, y, word_size_range=[20, 100],shape='diamond')
    wordcloud.render()
    os.system(r"render.html")
    
x = ['python', '爬虫', '人工智能', '大数据', 'Django','Flask',
     '机器学习', '数据分析', '深度学习', '运维测试', 'TensorFlow','Scrapy',
     'MySQL', '自然语言处理', 'NLP','数据处理','Github', '开放源码', 'Redis', '码云', '数据挖掘']
y = [10000, 6181, 4386, 4755, 2467, 2244, 1898, 1484, 1112,
 965, 847, 582, 565, 550, 62, 366, 3605, 2822, 273, 265,5000]

if __name__ == "__main__":
	wordcloud(x,y)

