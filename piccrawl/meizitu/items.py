# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    image_urls = scrapy.Field()  # 图片原图的地址
    images = scrapy.Field()  # 图片原图