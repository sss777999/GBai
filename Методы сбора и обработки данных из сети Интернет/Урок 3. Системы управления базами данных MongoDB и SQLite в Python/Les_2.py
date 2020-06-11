'''
1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
записывающую собранные вакансии в созданную БД
2) Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой
больше введенной суммы
3*)Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта
'''

# Задание 3.
# Логика работы двух файлов состоит в том, что в Les_1_updated собираются вакансии, делается датафрейм, после все
# заносится в data.csv, далее в Les_2 читается этот csv, hash проверяются на дублирования, недостающие добавляются
# в базу данных, также и архив сохраняется (если не будет идентичного объявления (можно было еще дату учесть, тогда
# бы и идентичные, но разные по дате, сохрянялись).
# о 3 задании расскажу вначале. Модернизировал файл предидущего урока, чтобы hash еще вставлял для каждой строки,
# добавляемой в df. В этом файле, в цикле по датафрейму берется хеш и find по коллекции в нашей базе данных, если
# есть, то drop строку из датафрейма. После очистки вставляются те, которых еще нет в нашей базе данных.
# Проверить можно введя в поле text, в файле Les_1_updated значение другой вакансии, проверял на ML. При повторном
# запуске новых вакансий не добавлялось. Крутое задание, было очень интересно все делать! Спасибо


import pandas as pd
from pymongo import MongoClient

count = 0
client = MongoClient('localhost', 27017)
db = client['hh']
vacancy = db.vacancy
df = pd.read_csv('data.csv', index_col=0)
df.drop('index', axis=1, inplace=True)
for i in df['hash']:
    g = vacancy.find_one({'hash': i})
    if vacancy.find_one({'hash': i}):
        idx = df.loc[df['hash'] == i].index[0]
        df = df.query(f"index != {idx}")
if df.empty:
    print('Нет новых вакансий')
else:
    count += 1
    records = df.to_dict(orient='records')
    result = db.vacancy.insert_many(records)

# Задание 2
# inp = float(70000)
inp = float(input('Введите минимальную интересующую сумму: '))

# Можно разделить на 2 find по min и max, чтобы было видно где это минииальная и где максимальная, или можно
# как-то в одной строке сделать вывод если min больше то выводить с min и по аналогии с max?
for c, _ in enumerate(vacancy.find({'$or': [{'min': {'$gte': inp}}, {'max': {'$gte': inp}}]},
                                   {'_id': 0, 'name': 1, 'min': 1, 'max': 1})):
    print(c, _)
