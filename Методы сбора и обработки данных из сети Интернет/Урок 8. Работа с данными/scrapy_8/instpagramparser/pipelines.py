# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient

class InstpagramparserPipeline:
    def __init__(self):
        # Если csv открыть файл на запись
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.inst_users_parser

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item
