# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PicCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    image_urls = scrapy.Field()  # 图片原图的地址
    images = scrapy.Field()  # 图片原图
    image_title = scrapy.Field()  # MM标题
    fileName = scrapy.Field()  # 文件夹名，每一个MM一个文件夹
    path = scrapy.Field()  # 图片存储路径（绝对路径）
