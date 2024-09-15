# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    """ Class representing Books Items"""

    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
