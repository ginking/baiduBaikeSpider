# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import datetime
import pymysql


class BaidubaikecitiaoPipeline(object):
    def __init__(self):
        dt = datetime.datetime.now()
        self.file = open('./info/' + dt.strftime('%Y-%m-%d') + '.json', 'w+')
        self.conn = pymysql.connect(
            host='127.0.0.1', user='root', passwd='666666')
        self.conn.query('create database if not exists baidu_citiao  ')
        self.conn.close()
        self.conn1 = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='666666',
            db='baidu_citiao',
            port=3306,
            charset='utf8')
        self.table_name = dt.strftime('%Y_%m_%d')
        self.conn1.query('drop table if exists ' + self.table_name)
        sql_create_table = 'create table ' + self.table_name + '(name char(20),browseNum int(32),editNum int(16),editUpdateTime char(10))'
        try:
            self.conn1.query(sql_create_table)
        except Exception as e:
            print(e)
        self.sql = 'insert into ' + self.table_name + '(name,browseNum,editNum,editUpdateTime) values("{name}","{browseNum}","{editNum}","{editUpdateTime}")'

    def process_item(self, item, spider):
        it = dict(item)
        self.file.write(json.dumps(it, ensure_ascii=False) + '\n')
        sql = self.sql.format(
            name=it['name'],
            browseNum=it['browseNum'],
            editNum=it['editNum'],
            editUpdateTime=it['editUpdateTime'])
        self.conn1.query(sql)
        self.conn1.commit()

    def close_spider(self, spider):
        self.file.close()
        self.conn1.close()
