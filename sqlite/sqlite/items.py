# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SqliteItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    release_date = scrapy.Field()
    version = scrapy.Field()
    filename = scrapy.Field()
    name_version = scrapy.Field()
    content = scrapy.Field()
    download_path = scrapy.Field()
    bundle_name = scrapy.Field()