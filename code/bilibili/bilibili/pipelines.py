# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#coding=utf-8
# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter

import pymongo
class BilibiliPipeline:

    # def __init__(self):#创建一个数据库对象
    #     self.client = pymongo.MongoClient(默认不用改的，端口号默认就是27017，ip就是我们本地的ip)
    #     self.db = self.client['bbbb']

    def __init__(self):
        self.file = open('bzhan.csv', 'w', newline='',encoding='utf-8')
        csv_fp = csv.writer(self.file)  # 处理成可用
        csv_fp.writerow(['title','play_num','ping_lun','user_name','score'])





    def process_item(self, item, spider):
        # print(type(item))
        data=dict(item)
        # print(item)
        # self.db.rank3.insert(data)


        # a = []
        # for headers in sorted(item.keys()):  # 把字典的键取出来
        #     a.append(headers)
        #     header = a  # 把列名给提取出来，用列表形式呈现


        csv_fp = csv.writer(self.file)  # 处理成可用

        list = []
        for i in data.values():
           list.append(i)
        # print(list)
        csv_fp.writerow(list)#上面1234要和个数匹配


        # csv_fp = csv.writer(self.file)  # 处理成可用
        # csv_fp.writerow((data['title'],data['play_num']))

        return item


