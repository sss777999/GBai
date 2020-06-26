# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import MapCompose, TakeFirst
import scrapy
import json


def cleaner_price(value):
    val = ''.join(value).replace(' ', '')
    val = int(val)
    return val


def cleaner_characteristics(characteristic):
    for i in range(len(characteristic)):
        characteristic[i] = characteristic[i].replace('\n', '').replace('  ', '')
    d = {}
    lst = []
    for i in characteristic:
        if i:
            lst.append(i)
    for i in range(len(lst)):
        if i % 2 == 0:
            d[lst[i]] = lst[i + 1]
    return d


class LeruaparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=cleaner_price)
    photos = scrapy.Field()
    characteristic = scrapy.Field(input_processor=cleaner_characteristics)
    link = scrapy.Field()
