# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from meizitu.items import MeizituItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['www.plmm.com.cn']
    start_urls = ['https://www.plmm.com.cn/xiaohua/']

    """
    处理校花类，主页面中的各个妹妹的家
    得到她们家的地址sites
    """
    def parse(self, response):
        sel = Selector(response)
        sites = sel.css("div.content div.goods-item a::attr(href)").extract()
        for siteUrl in sites:
            print('siteUrl')
            url = response.urljoin('https:' + siteUrl.split('.html')[0] + '/')
            yield scrapy.Request(url, self.parse_page2)

        # 校花大类页面的翻页
        hrefs = sel.css("div.content div.good-list-box ul.pagination a.page-num::attr(href)").extract()
        for href in hrefs:
            url2 = response.urljoin('https://www.plmm.com.cn' + href)
            yield scrapy.Request(url2, self.parse)

    """到一个妹妹家中找到，她详细的每一张照片的地址"""
    def parse_page2(self, response):
        item = MeizituItem()
        sel = Selector(response)
        sites = sel.css("div.content div.main article img::attr(src)").extract()
        names = sel.css("div.content div.main h1::text").extract()
        for siteUrl in sites:
            print('siteUrl')
            item['image_urls'] = ['https:' + siteUrl]  # 特别注意，不这么处理会产生错误。
            item['name'] = names
            yield item

        # 各个图片集合的翻页
        hrefs = sel.css("div.content div.main a.page-num::attr(href)").extract()
        for href in hrefs:
            url = response.urljoin('https:' + href)
            yield scrapy.Request(url, self.parse_page2)
