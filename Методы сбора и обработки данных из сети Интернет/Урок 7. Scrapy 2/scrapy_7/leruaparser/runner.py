'''
1) Взять любую категорию товаров на сайте Леруа Мерлен. Собрать с использованием ItemLoader следующие данные:
● название;
● все фото;
● параметры товара в объявлении;
● ссылка;
● цена.

С использованием output_processor и input_processor реализовать очистку и преобразование данных.
Цены должны быть в виде числового значения.

2)Написать универсальный обработчик параметров объявлений, который будет формировать данные вне
зависимости от их типа и количества.

3)*Реализовать хранение скачиваемых файлов в отдельных папках, каждая из которых должна соответствовать
собираемому товару
'''

# из images все удалил, чтобы лишнее не загружать
# появился нюанс с mongo, все работает и через терминал запускается, а база не создается, тут все прозходит без ошибок,
# и инсерты и т.д., но почему-то даже в дебаггере где колекцию создаю, все прозодит, но сама база и коллекция не
# не создалась. Обновлений никаких не усаналвивал на Mac, после прошлого обновления половниу дня потратил
# на то. чтобы можно с mongo было что-то делать, по умолчанию блокирует db path. Может это с этим связано?

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leruaparser import settings
from leruaparser.spiders.lerua import LeruaSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeruaSpider, search='бензопилы')
    process.start()
