# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from urllib.parse import urlparse
from pymongo import MongoClient


class LeruaparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.leroy_merlin

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        ggggg = spider.name
        list = []
        for i in item:
            dict = {}
            dict[i] = item[i]
            list.append(dict)
        collection.insert_one(list)
        # сюда добавить добавление в бд
        return item


class LeruaPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img, meta=item)  # meta=item
                except Exception as e:
                    print(e)

    def file_path(self, request, response=None, info=None):
        item = request.meta
        pathname = item["name"][:30]
        return pathname + '/' + os.path.basename(urlparse(request.url).path)

    # def item_completed(self, results, item, info):
    #     if results:
    #         item['photos'] = [itm[1] for itm in results if item[0]]
    #     return item  # важно
