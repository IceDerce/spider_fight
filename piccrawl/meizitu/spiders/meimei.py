# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from meizitu.items import MeizituItem


class MeizituSpider(scrapy.Spider):
    name = 'meimei'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/']

    """
    def start_requests(self):
        # 先爬取前6页
        for i in range(2, 3):
            url = 'http://www.mmjpg.com/home/' + str(i)
            yield scrapy.Request(url, callback=self.parse_page1)
    """
    def parse(self, response):
        for href in response.css("div.pic a::attr(href)"):
            yield response.follow(href, self.parse_page2)
            # l1 = ItemLoader(item=MeizituItem(), response=response)
            # l1.add_css("fileName", "div.pic span.title a")


        # 以下语句即可代替翻页函数
        # for href in response.css("div.page a::attr(href)"):
        #    yield response.follow(href, self.parse_page1)

    def parse_page2(self, response):

        """
        relativepath = "/home/zeaslity/Pictures/zhihu/"
        l = ItemLoader(item=MeizituItem(), response=response)
        l.add_css("image_urls", "div.content a img::attr(src)")
        l.add_css("image_title", "div.page em")

        l.add_value("path", '/home/zeaslity/Pictures/zhihu/ + response.meta['fileName']')
        """
        for href in response.css("div.page a::attr(href)"):
            yield {
                'image_urls': response.xpath("/html/body/div[2]/div[1]/div[2]/a/img/@src").extract()[0]
            }
            yield response.follow(href, self.parse_page2)
