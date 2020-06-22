'''
I вариант
1) Доработать паука в имеющемся проекте, чтобы он формировал item по структуре:
*Наименование вакансии
*Зарплата от
*Зарплата до
*Ссылку на саму вакансию

*Сайт откуда собрана вакансия
И складывал все записи в БД(любую)

2) Создать в имеющемся проекте второго паука по сбору вакансий с сайта superjob. Паук должен формировать item'ы по аналогичной структуре и складывать данные также в БД

II вариант
1) Создать двух пауков по сбору данных о книгах с сайтов labirint.ru и book24.ru
2) Каждый паук должен собирать:
* Ссылку на книгу
* Наименование книги
* Автор(ы)
* Основную цену
* Цену со скидкой
* Рейтинг книги
3) Собранная информация дожная складываться в базу данных
'''

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from hhparser import settings
# 1
from hhparser.spiders.hhruparse import HhruparseSpider
# 2
from hhparser.spiders.sj import SjSpider

# 2 паук
# from jobparser.spiders.hhruparse import SjruSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    # 1
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruparseSpider)

    # 2
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(SjSpider)
    # создать сначала второго паука
    # для второго паука
    # process.crawl(SjSpider)
    process.start()
