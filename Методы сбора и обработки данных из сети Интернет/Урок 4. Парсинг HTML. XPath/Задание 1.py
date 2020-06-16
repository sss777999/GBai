'''
1)Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex.news
Для парсинга использовать xpath. Структура данных должна содержать:
название источника,
наименование новости,
ссылку на новость,
дата публикации

2)Сложить все новости в БД
'''

# В функции yandex добываются еще оригинальные линки, которые через еще один get получаются, но нужно подождать
# секунд 30 пока все запросы на каждую новость пройдут. В yandex сохранил 'original_source, date': 'Evo-rus.com 09:41',
# время там с названием ресурса вместе идет, даты нет, пытался из первоисточника вытягивать, но там разные ресуры
# и разные теги, можно конечно их все, что есть проанализировать и вытянуть, но думаю, что это лишнее.

from pprint import pprint
from lxml import html
import requests
import json
from pymongo import MongoClient

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
links = []


def mail():
    global links
    response = requests.get('https://news.mail.ru', headers=header)
    dom = html.fromstring(response.text)
    # верхняя часть с 5 фотографиями
    names = dom.xpath(
        "//span[contains(@class, 'photo__title photo__title_new photo__title_new_hidden js-topnews__notification')]/text()")
    links = dom.xpath("//a[contains(@class,'js-topnews__item')]/@href")
    for i in range(len(names)):
        item = {}
        source = 'Mail.ru'
        item['source'] = source
        item['name'] = names.pop(0)
        item['link'] = "https://news.mail.ru" + links.pop(0)
        l = str(item['link'])
        date = requests.get(l, headers=header)
        d = html.fromstring(date.text)
        datetime = d.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
        item['date'] = datetime
        links.append(item)
    # под ними ниже 6 новостей
    # почему-то дублируются 2 из последние из верхних сюда, как их исключить?
    names2 = dom.xpath("//a[@class='list__text']/text()")
    links2 = dom.xpath("//a[@class='list__text']/@href")
    for i in range(len(names2)):
        item2 = {}
        source2 = 'Mail.ru'
        item2['source'] = source2
        item2['name'] = names2.pop(0)
        item2['link'] = "https://news.mail.ru" + links2.pop(0)
        l2 = str(item2['link'])
        date2 = requests.get(l2, headers=header)
        d2 = html.fromstring(date2.text)
        datetime2 = d2.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
        item2['date'] = datetime2
        links.append(item2)


mail()


def lenta():
    global links
    response = requests.get('https://lenta.ru', headers=header)
    dom = html.fromstring(response.text)
    names = dom.xpath("//div[@class='item'] | a[@href]")
    for i in names:
        item = {}
        source = 'Lenta.ru'
        item['source'] = source
        item['name'] = i.xpath(".//div[@class='item'] | a[@href]/text()")
        item['link'] = "https://lenta.ru" + str(i.xpath(".//div[@class='item'] | a[@href]/@href"))
        item['date'] = i.xpath(".//div[@class='item'] | a[@href]/@title")
        links.append(item)


lenta()


def yandex():
    global links
    response = requests.get('https://yandex.ru/news', headers=header)
    dom = html.fromstring(response.text)
    names = dom.xpath("//a[contains(@class, 'link link_theme_black i-bem')]/text()")
    link = dom.xpath(".//a[contains(@class, 'link link_theme_black i-bem')]/@href")
    time = dom.xpath("//div[contains(@class, 'story__date')]/text()")
    for i in range(len(names)):
        item = {}
        source = 'Yandex.ru'
        item['source'] = source
        item['name'] = names.pop(0)
        l = "https://yandex.ru" + link.pop(0)
        # item['link'] = l
        lget = requests.get(l, headers=header)
        d = html.fromstring(lget.text)
        dlink = d.xpath("//a[@class='link link_theme_grey link_agency i-bem']/@href")
        item['link'] = "".join(dlink)
        item['original_source, date'] = time.pop(0)
        links.append(item)


yandex()

'''for _, i in enumerate(links):
    print(_, i)'''

# сохранить в json
with open("news.json", "w", encoding="utf-8") as file:
    json.dump(links, file)

# загрузить из json
with open('news.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    print(text)

client = MongoClient('localhost', 27017)
db = client['news_gb']
news = db.news
news.insert_many(text), {'upsert': True}
