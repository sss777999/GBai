'''
1)Написать приложение, которое будет проходиться по указанному списку двух и/или более пользователей
и собирать данные об их подписчиках и подписках.
2) По каждому пользователю, который является подписчиком или на которого подписан исследуемый объект
нужно извлечь имя, id, фото (остальные данные по желанию). Фото можно дополнительно скачать.
3) Собранные данные необходимо сложить в базу данных. Структуру данных нужно заранее продумать, чтобы:
4) Написать запрос к базе, который вернет список подписчиков только указанного пользователя
5) Написать запрос к базе, который вернет список профилей, на кого подписан указанный пользователь
'''

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from instpagramparser import settings
from instpagramparser.spiders.instagram import InstagramSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(InstagramSpider)
    process.start()

# ТОЛЬКО ТАК РАБОТАЕТ InstpagramparserItem!!!
#
# /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/scrapy/item.py
# В 80 строке изменения внести
#     def __init__(self, *args, **kwargs):
#         self._values = {}
#         if args or kwargs:  # avoid creating dict for most common case
#             for k, v in dict(*args, **kwargs).items():
#                 self[k] = v # оригинал
#                 self._values[k] = v # только с такой заменой работает!
