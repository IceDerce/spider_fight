# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()  # 每一张图片的地址
    image_paths = scrapy.Field()  # 每一张图片的保存位置
    name = scrapy.Field()  # 每张图片的名称
