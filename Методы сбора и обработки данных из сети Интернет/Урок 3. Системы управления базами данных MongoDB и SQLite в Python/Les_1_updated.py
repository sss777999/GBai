'''
1) Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайта superjob.ru и hh.ru. Приложение должно анализировать несколько страниц сайта(также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:

    *Наименование вакансии
    *Предлагаемую зарплату (отдельно мин. и отдельно макс.)
    *Ссылку на саму вакансию
    *Сайт откуда собрана вакансия
'''
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import hashlib

# чтобы смотреть колонки датафрейма
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
# ---------------------------------

main = 'https://krasnogorsk.hh.ru/'
page = 0
vac = []
count = 1
while True:
    params = {'text': 'Artificial Intelligence',  # то, что тут + не нужен кардинально меняет ситуацию! Тут указывал ML
              # для проверки на повторения
              'fromSearch': 'true',
              'area': '1',
              'st': 'searchVacancy',
              'page': f'{page}'}  # на каждой итерации прибавляем +1 к странице
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    response = requests.get(main + 'search/vacancy', headers=headers, params=params)
    soup = bs(response.text, 'lxml')
    vacansies_block = soup.find('div', {'class': 'vacancy-serp'})
    vacansies_list = vacansies_block.findChildren(recursive=False)
    pattern = r'\w{2}.ru'  # берем название сайта
    for i in vacansies_list:
        if i['class'] == ['vacancy-serp-item'] or i['class'] == ['vacancy-serp-item', 'vacancy-serp-item_premium']:
            name = i.find('a', {'class': 'bloko-link HH-LinkModifier'}).text
            url = i.find('a', {'class': 'bloko-link HH-LinkModifier'})['href']
            site = str(re.findall(pattern, url)).strip('[]').strip("'")  # можно как-то проще было это сделать?
            try:
                salary = i.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text
            except AttributeError:
                salary = 'None'
            # добавим hash, чтобы потом не добавлять в бд данные с таким же hash
            vac.append([count, name, salary, url, site, hashlib.sha1
            (str([count, name, salary, url, site]).encode('utf-8')).hexdigest()])
            # count оставлю на всякий случай
            count += 1
    page += 1
    # если нет кнопки дальше, то break
    if not soup.find('a', {'class': 'bloko-button HH-Pager-Controls-Next HH-Pager-Control'}):
        break
# убираем этот знак u'\xa0', почему он вообще там появляется и только после print, так его не видно в дебаггере даже?
# разбиваем на от, до, суммы, валюта
for i in vac:
    if i[2] != 'None':
        i[2] = i[2].replace(u'\xa0', '')
        if '-' in i[2]:
            i[2] = i[2].replace('-', ' ').split(' ')
            ggg = i[2]
        else:
            i[2] = i[2].split(' ')
# делаем датафрейм
data = pd.DataFrame(vac, columns=['index', 'name', 'salary', 'uri', 'site', 'hash'])
for i in vac:
    if i[2] != 'None':
        if len(i[2]) > 2 and i[2][0] != 'до' and i[2][0] != 'от':
            data.loc[data['name'] == i[1], 'min'] = i[2][0]
            data.loc[data['name'] == i[1], 'max'] = i[2][1]
        data.loc[data['name'] == i[1], 'currency'] = i[2][-1]
        if len(i[2]) > 2 and i[2][0] == 'от':
            data.loc[data['name'] == i[1], 'min'] = i[2][1]
        if len(i[2]) > 2 and i[2][0] == 'до':
            data.loc[data['name'] == i[1], 'max'] = i[2][1]
data.drop('salary', axis=1, inplace=True)  # salary можно не drop и проверить, по этому слобцу сравнивал значения
print(data)
# на SuperJob таких вакансий нет ) думал тоже попробовать.

data.to_csv('data.csv', encoding='utf-8')
