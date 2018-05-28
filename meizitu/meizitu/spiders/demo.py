# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from meizitu.items import MeizituItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    start_urls = ['https://www.plmm.com.cn/xinggan/2878/']

    def parse(self, response):
        item = MeizituItem()
        sel = Selector(response)
        sites = sel.css("div.main article img::attr(src)").extract()
        for siteUrl in sites:
            print('siteUrl')
            item['image_urls'] = ['https:' + siteUrl]  # 特别注意，不这么处理会产生错误。
            yield item

        for href in response.css("div.page a::attr(href)"):
            yield response.follow(href, self.parse)
