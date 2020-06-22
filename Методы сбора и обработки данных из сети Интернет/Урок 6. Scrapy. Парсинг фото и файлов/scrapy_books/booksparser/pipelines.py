# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class BooksparserPipeline:
    def __init__(self):
        # Если csv открыть файл на запись
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.books_labirint_book24

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        if len(item['price']) > 1 and item['price'][0].isdigit():
            item['price'] = {'new_price': item['price'][0],
                             'old_price': item['price'][1]
                             }
        else:
            item['price'] = ''.join(item['price'])
        collection.insert_one(item)
        return item
