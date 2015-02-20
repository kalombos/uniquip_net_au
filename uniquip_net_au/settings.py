# -*- coding: utf-8 -*-

# Scrapy settings for uniquip_net_au project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'none'

SPIDER_MODULES = ['uniquip_net_au.spiders']
NEWSPIDER_MODULE = 'uniquip_net_au.spiders'
ITEM_PIPELINES = {
    'uniquip_net_au.pipelines.ImagePipeline': 1
}
IMAGES_STORE = '/home/kalombo/projects/uniquip_net_au/images'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) ' \
             'Gecko/20100101 Firefox/35.0'

FEED_EXPORTERS = {
    'csv': 'uniquip_net_au.csv_exporter.OrderCsvItemExporter',
}
FIELDS_TO_EXPORT = ['product_url', 'product_title', 'product_image']