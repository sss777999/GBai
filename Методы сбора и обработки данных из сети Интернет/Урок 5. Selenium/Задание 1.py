'''
1) Написать программу, которая собирает входящие письма из своего или тестового почтового
ящика и сложить данные о письмах в базу данных
* от кого,
* дата отправки,
* тема письма,
* текст письма полный

Логин тестового ящика: study.ai_172@mail.ru
Пароль тестового ящика: NextPassword172
'''

# после print list все правильно, проверил, а вот в базе через Compass смотрю количество правильное,
# но почему-то первые три время стоит 20:08. Также и в json файле. Почему непонятно. Почему upsert тогда не сработал?
# Все работает очень не стабильно, долго, по time.sleep нужно угадывать, каждый раз
# по-разному может понадобиться времени.
# через find_element_by_class_name находит через раз, по какой причине непонятно. Решилось случайно ущзнав
# от одногрупника что из письма можно дальше листать. С прокруткой не рабоатет тут, на других сайтах без проблем.
# Потрачено было около 10 часов на это задание.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
from pymongo import MongoClient

list = []
chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get('https://mail.ru/')
elemlog = driver.find_element_by_id('mailbox:login')
elemlog.send_keys('study.ai_172@mail.ru')  # можно и без mail.ru
button1 = driver.find_element_by_class_name('o-control')
button1.submit()
time.sleep(2)

elempass = driver.find_element_by_id('mailbox:password')
elempass.send_keys('NextPassword172')
button2 = driver.find_element_by_class_name('o-control')
button2.submit()
time.sleep(3)
let = driver.find_element_by_xpath(
    "//a[@class='llc js-tooltip-direction_letter-bottom js-letter-list-item llc_pony-mode llc_normal']").click()
while True:
    time.sleep(0.5)
    d = {}
    letfr = driver.find_element_by_class_name('letter-contact').text
    letdate = driver.find_element_by_class_name('letter__date').text
    lettext = driver.find_element_by_xpath("//div[@class='letter__body']").text
    lettheme = driver.find_element_by_xpath("//div[@class='thread__header']").text
    d['from'] = letfr
    d['date'] = letdate
    d['text'] = lettext
    d['theme'] = lettheme
    list.append(d)
    but = driver.find_element_by_xpath(
        "//div[@class='portal-menu-element portal-menu-element_next portal-menu-element_expanded portal-menu-element_not-touch portal-menu-element_pony-mode']").click()
    time.sleep(0.3)
    g = driver.find_elements_by_xpath("//span[contains(@class,'disabled')]")
    if g:
        driver.quit()
        break

print(len(list))
for _, i in enumerate(list):
    print(_, i)

with open("mail.json", "w", encoding="utf-8") as file:
    json.dump(list, file)

# загрузить из json
with open('mail.json', 'r', encoding='utf-8') as f:
    text = json.load(f)

client = MongoClient('localhost', 27017)
db = client['mail']
mail = db.mail
mail.insert_many(text), {'upsert': True}
