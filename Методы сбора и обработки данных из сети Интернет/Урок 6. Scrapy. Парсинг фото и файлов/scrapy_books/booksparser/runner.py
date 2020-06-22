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

# По очереди если запускать работает отлично, по 2 одновременно, когда 1 заканчивает, тогда и второй,
# в settings добавлял еще другую pipeline, добавлял классы, без разницы. Наследовал init. Как правильно это делать?
# Чтобы 2 работали одновременно. Получается что все попадает в pipelines через items, чтобы там не писал все равно
# в pipelines попадает в один класс. Как нужно настраивать?

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from booksparser import settings
# 1
from booksparser.spiders.labirintparser import LabirintparserSpider
# 2
from booksparser.spiders.book24parser import Book24parserSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    # 1
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LabirintparserSpider)

    # 2
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(Book24parserSpider)

    process.start()
