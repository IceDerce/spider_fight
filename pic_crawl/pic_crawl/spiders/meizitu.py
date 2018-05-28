# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from pic_crawl.pic_crawl.items import PicCrawlItem


class PicCrawlSpider(scrapy.Spider):
    name = 'PicCrawl'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/']

    def start_requests(self):
        # 先爬取前6页
        for i in range(2, 3):
            url = 'http://www.mmjpg.com/home/' + str(i)
            yield scrapy.Request(url, callback=self.parse_page1)

    def parse_page1(self, response):
        for href in response.css("div.pic a::attr(href)"):
            l = ItemLoader(item=PicCrawlItem())
            l.add_css("fileName", "div.pic span.title a")
            yield response.follow(href, self.parse_page2)

        # 以下语句即可代替翻页函数
        # for href in response.css("div.page a::attr(href)"):
        #    yield response.follow(href, self.parse_page1)

    def parse_page2(self, response):
        relativepath = "/home/zeaslity/Pictures/zhihu/"
        l = ItemLoader(item=PicCrawlItem())
        l.add_css("image_urls", "div.content a img::attr(src)")
        l.add_css("image_title", "div.page em")
        path = relativepath + l.get_value("fileName")
        l.add_value("path", path)

        for href in response.css("div.page a::attr(href)"):
            yield response.follow(href, self.parse_page2)
