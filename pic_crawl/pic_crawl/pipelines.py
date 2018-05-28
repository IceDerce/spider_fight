# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os


class MeiZiTuPipeline(object):
    def process_item(self, item, spider):
        image_urls = item['image_urls']
        path = item['path']
        fileName = item['fileName']

        for image_url in image_urls:
            if not os.path.exists(fileName):
                os.makedirs(fileName)
            image = requests.get(image_url)
            f = open(path, 'wb')
            f.write(image.content)
            f.close()
            print("正在保存图片", image_urls)
            print("图片路径", path)
            print("文件", fileName)

        return item
