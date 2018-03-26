# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy import Request
from baiduBaikeCiTiao.items import BaidubaikecitiaoItem
import re
import json

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']

    info_url = 'http://baike.baidu.com/item/{ciTiao}'
    browseNum_url = 'http://baike.baidu.com/api/lemmapv?id={id}'
    hrefPat = re.compile('href="/item/(.*?)"')
    idPat = re.compile('newLemmaIdEnc:"(.*?)"')
    updateTimePat = re.compile('最近更新：.*?>(.*?)<')
    editNumPat = re.compile('编辑次数：(.*?)次')
    namePat = re.compile('dd class="lemmaWgt-lemmaTitle-title">.*?<h1 >(.*?)</h1>',re.S)

    ciTiao = 'Python'
    # ciTiao = urllib.request.quote(ciTiao)

    def start_requests(self):
    	yield Request(self.info_url.format(ciTiao=self.ciTiao),meta={'cookiejar':1},callback = self.parse,dont_filter=False)


    def parse(self, response):
    	item = BaidubaikecitiaoItem()
    	item['editNum'] = int(self.editNumPat.findall(response.text)[0])
    	item['editUpdateTime'] = self.updateTimePat.findall(response.text)[0]
    	item['name'] = self.namePat.findall(response.text)[0]
    	data = json.loads(urllib.request.urlopen(self.browseNum_url.format(id=self.idPat.findall(response.text)[0])).read().decode('utf-8'))
    	item['browseNum'] = data['pv']

    	yield item 
    	
    	for ciTiao in self.hrefPat.findall(response.text):
    		yield Request(self.info_url.format(ciTiao=ciTiao),meta={'cookiejar':response.meta['cookiejar']},callback=self.parse,dont_filter=False)

    	
    	
    	
        
