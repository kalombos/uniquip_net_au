# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ProductItem(scrapy.Item):
    product_url = Field()
    product_title = Field()
    product_image = Field()