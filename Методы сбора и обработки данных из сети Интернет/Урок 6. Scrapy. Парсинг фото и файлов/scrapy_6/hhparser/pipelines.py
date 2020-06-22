# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


# для обработки

class HhparserPipeline:
    def __init__(self):
        # Если csv открыть файл на запись
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancies_hh_sj_scrapy

    def process_item(self, item, spider):
        dict_vacancy = {}
        collection = self.mongo_base[spider.name]
        dict_vacancy['name'] = item['name']
        # dict_vacancy['salary'] = ' '.join(item['salary']).replace('  ', ',').split(',')
        dict_salary = ' '.join(item['salary']).replace(u'\xa0', '').replace('  ', ',').split(',')
        try:
            if dict_salary[0] == 'от' and dict_salary[2] == 'до':
                dict_vacancy['salary'] = {'from': dict_salary[1].replace(u'\xa0', ''),
                                          'to': dict_salary[3].replace(u'\xa0', '')
                                          }
            elif dict_salary[0] == 'до':
                dict_vacancy['salary'] = {'from': '-',
                                          'to': dict_salary[1].replace(u'\xa0', '')
                                          }
            elif dict_salary[0] == 'от':
                dict_vacancy['salary'] = {'from': dict_salary[1].replace(u'\xa0', ''),
                                          'to': '-'
                                          }
            else:
                dict_vacancy['salary'] = ''.join(dict_salary)
        except:
            pass

        dict_vacancy['link'] = item['link']
        collection.insert_one(dict_vacancy)
        return item

    # def __del__(self):
    #     pass
    #     файл close

# новый класс в pipelines
