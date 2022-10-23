import scrapy
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

import math
class DanmuSpider(scrapy.Spider):
    name = 'danmu'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://api.bilibili.com/x/v1/dm/list.so?oid=226204073']


    def parse(self, response):

        test=response.xpath("//d//text()").extract()
        fp=open('bzhanzzzvvvvvvv.csv','w',encoding='utf-8')
        csv_fp=csv.writer(fp)#处理成可用
        for i in test:
            item=[i]
            csv_fp.writerow(item)
            print(item)


