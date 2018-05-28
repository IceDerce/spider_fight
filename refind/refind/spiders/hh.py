# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from refind.items import RefindItem


class HhSpider(scrapy.Spider):
    name = 'hh'
    start_urls = ['http://www.mmjpg.com/mm/1362']

    def parse(self, response):
        item = RefindItem()
        sel = Selector(response)
        sites = sel.css("div.main div.article div.content a img::attr(src)").extract()
        for siteUrl in sites:
            print('siteUrl')
            item['image_urls'] = ['' + siteUrl]  # 特别注意，不这么处理会产生错误。
            yield item

        hrefs = sel.css("div.main div.article div.page a.ch\000next::attr(href)").extract()
        for href in hrefs:
            picurl = ['http://www.mmjpg.com' + href]
            url = response.urljoin(picurl)
            yield scrapy.Request(url, self.parse)

