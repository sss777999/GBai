# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InstpagramparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    username = scrapy.Field()
    user_id_subscribers = scrapy.Field()
    follow_by_user_id = scrapy.Field()
    info_user_name = scrapy.Field()
    info_full_user_name = scrapy.Field()
    photo = scrapy.Field()
    status = scrapy.Field()
    status_verified = scrapy.Field()
    post_ = scrapy.Field()
