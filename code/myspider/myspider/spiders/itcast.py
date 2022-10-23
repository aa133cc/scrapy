import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
       # rea = response.xpath("//div[@class='tea_con']//h3/text()").extract()
       # print(rea)

       li_list=response.xpath("//div[@class='tea_con']//li")
       # item=dict(li_list)
       for li in li_list:
          item={}
          item["name"]= li.xpath(".//h3/text()").extract_first()
          item["title"]= li.xpath(".//h4/text()").extract_first()
          #print(item)
          yield item

