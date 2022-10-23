import scrapy


class BizhanSpider(scrapy.Spider):
    name = 'bizhan'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='rank-list-wrap']//li")  # 犯过错误

        for tr in tr_list:
            item = {}
            item["title"] = tr.xpath(".//a[@class='title']/text()").extract_first()
            item["play_num"] = tr.xpath(
                "normalize-space(.//div[@class='detail']/span[@class='data-box'][1]/text())").extract_first()
            item["ping_lun"] = tr.xpath("normalize-space(.//span[@class='data-box'][2]/text())").extract_first()
            item["user_name"] = tr.xpath("normalize-space(.//div[@class='detail']/a/span/text())").extract_first()
            yield item