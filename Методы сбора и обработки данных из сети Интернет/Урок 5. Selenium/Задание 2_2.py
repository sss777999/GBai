# ВАРИАНТ 2


'''
3) Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД.
Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары
'''

# как тут правильно обработать дата чтобы занести в базу данных? По-моему оказалось это не словарь в data-product-info,
# по type - это str. Просто внешне там выглядит как словарь. Объясните пожалуйста, как тут сделать правильно,
# чтобы в базу занести!!!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient
import json

list = []
chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver.get('https://www.mvideo.ru/')
time.sleep(3)
button_next = driver.find_elements_by_xpath('//a[@class="next-btn sel-hits-button-next"]')

while True:
    elem = driver.find_elements_by_xpath('//ul[@class="accessories-product-list"]')
    tov = elem[2].find_elements_by_xpath(".//a[@class='sel-product-tile-title']")
    but_not_active = driver.find_elements_by_xpath("//a[@class='next-btn sel-hits-button-next disabled']")
    button_next[1].click()
    time.sleep(2)
    if but_not_active:
        for i in tov:
            data = i.get_attribute('data-product-info')
            jdata = json.loads(data)
            print(jdata)
            print(type(jdata))
            list.append(jdata)
        driver.quit()
        break

client = MongoClient('localhost', 27017)
db = client['hits']
hits = db.hits
hits.insert_many(list), {'upsert': True}
