# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy import Request


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['product_image'])

    def item_completed(self, results, item, info):
        images = [x for ok, x in results if ok]
        if images:
            image = images[0]
            path = image['path'].split('/')[-1]
            item['product_image'] = path
        return item
