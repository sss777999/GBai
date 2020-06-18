# ВАРИАНТ 1


'''
3) Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД.
Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары
'''
# как собрать конкретно указано не было, поэтому собрал в per_page информацию и продуктах
# все вместе по каждоый странице целиком. Получилось 4 страницы.
# Если сделать прокрутку и попытаться собрать все хиты сразу, они добавляются динамически
# после прокрутки на следующую страницу, то блокирует Max retries exceeded with url. Задним числом нельзя )

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient

list = []
chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver.get('https://www.mvideo.ru/')
time.sleep(3)
button = driver.find_elements_by_xpath('//a[@class="next-btn sel-hits-button-next"]')

while True:
    elem = driver.find_elements_by_xpath('//ul[@class="accessories-product-list"]')
    tov = elem[2].find_elements_by_xpath("//a[@class='sel-product-tile-title']")
    for i in tov:
        d = {}
        jk = i.get_attribute('data-product-info')
        if i.text:
            d['item'] = i.text
            list.append(d)

    g = driver.find_elements_by_xpath("//a[@class='next-btn sel-hits-button-next disabled']")
    button[1].click()
    time.sleep(2)
    if g:
        driver.quit()
        break

for i in list:
    print(i)

client = MongoClient('localhost', 27017)
db = client['hits']
hits = db.hits
hits.insert_many(list), {'upsert': True}
