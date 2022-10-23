import scrapy

from bilibili.items import BilibiliItem
class BiliSpider(scrapy.Spider):##这里面就有一个类。继承自scrapy.Spider
    name = 'bili'   #我们自己定义爬虫名
    allowed_domains = ['bilibili.com']    #允许爬取的范围,不能爬取到别的网站
    start_urls = ['https://www.bilibili.com/v/popular/rank/all']   #爬取的网页，最开始的url地址

    def parse(self, response):#处理start_urls地址对应的响应，我们提取数据

        tr_list=response.xpath("//div[@class='rank-list-wrap']//li") #犯过错误
        for tr in tr_list:
            i={}
            i["title"] = tr.xpath(".//a[@class='title']/text()").extract_first()#提取到的第一的字符串
            i["play_num"]=tr.xpath("normalize-space(.//div[@class='detail']/span[@class='data-box'][1]/text())").extract_first()
            i["ping_lun"] = tr.xpath("normalize-space(.//span[@class='data-box'][2]/text())").extract_first()
            i["user_name"] = tr.xpath("normalize-space(.//div[@class='detail']/a/span/text())").extract_first()
            i["score"] = tr.xpath("normalize-space(.//div[2]/div[2]/div[2]/div/text())").extract_first()
            yield i #交给我们的管道去处理，减少内存的占用，他是一个生成器





