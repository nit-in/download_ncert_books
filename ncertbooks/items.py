# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NcertbooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tclass_field = scrapy.Field()
    tsubject_field = scrapy.Field()
    tbook_field = scrapy.Field()
    tbook_link = scrapy.Field()
