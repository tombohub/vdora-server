# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SaleItem(scrapy.Item):
    date = scrapy.Field()
    sale_id = scrapy.Field()
    sku = scrapy.Field()
    product = scrapy.Field()
    quantity = scrapy.Field()
    price_per_unit = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
