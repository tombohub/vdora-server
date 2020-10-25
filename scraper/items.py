# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Sale(scrapy.Item):
    id = scrapy.Field()
    date = scrapy.Field()
    product = scrapy.Field()
    sku = scrapy.Field()
    quantity = scrapy.Field()
    price = scrapy.Field()
