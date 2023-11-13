# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import scrapy

class MovieItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    other_title = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    director_and_actors = scrapy.Field()
    rating = scrapy.Field()
    reviewers = scrapy.Field()
    quote = scrapy.Field()
