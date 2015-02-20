# -*- coding: utf-8 -*-
import scrapy
from uniquip_net_au.items import ProductItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["uniquip.net.au"]
    start_urls = (
        'http://uniquip.net.au/',
    )

    def parse(self, response):
        for url in response.xpath('//a[@class="list_bg_sub"]/@href').extract():
            yield scrapy.Request(url, callback=self.products_page)

    def products_page(self, response):
        xpath = '//div[@class="product_list_content"]/div/h3/a/@href'
        for url in response.xpath(xpath).extract():
            yield scrapy.Request(url, callback=self.product_page)

    def product_page(self, response):
        item = ProductItem()
        item['product_url'] = response.url
        xpath = '(//div[@itemprop="name"]/h2/text())[1]'
        item['product_title'] = ''.join(response.xpath(xpath).extract())
        xpath = '//div[@itemprop="description"]//img/@src'
        image_urls = response.xpath(xpath).extract()
        if image_urls:
            item['product_image'] = image_urls[0]
            yield item
