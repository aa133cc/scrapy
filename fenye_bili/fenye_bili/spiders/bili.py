import scrapy


class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/v/dance/otaku#/all/default/1']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='vd-list-cnt']//ul//li")  # 犯过错误
        for tr in tr_list:
            item = {}
            item["title"] = tr.xpath("//*[@id='videolist_box']/div[2]/ul/li[1]/div/div[2]/a")  # 提取到的第一的字符串
            # item["play_num"] = tr.xpath(
            #     "normalize-space(.//div[@class='detail']/span[@class='data-box'][1]/text())").extract_first()
            # item["ping_lun"] = tr.xpath("normalize-space(.//span[@class='data-box'][2]/text())").extract_first()
            # item["user_name"] = tr.xpath("normalize-space(.//div[@class='detail']/a/span/text())").extract_first()
            print(item)  # 交给我们的管道去处理，减少内存的占用，他是一个生成器
