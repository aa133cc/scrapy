import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['']
    start_urls = ['https://www.baidu.com/s?tn=88093251_103_hao_pg&ie=utf-8&wd=%E6%95%85%E5%AE%AB']

    def parse(self, response):
        data = response.xpath("//*[@id='2']/div/div[3]/p[1]/text()[4]").extract_first()
        print(data)
        with open('baidu.html', 'w', encoding='utf-8')  as f:
            f.write(response.body.decode('utf-8'))

