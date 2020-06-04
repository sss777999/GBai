'''
1. Посмотреть документацию к API GitHub, разобраться как вывести
список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
'''

import requests

user = "RMORIOKA"
main_link = f'https://api.github.com/users/{user}/repos'
response = requests.get(main_link)

print(f'Репозитории пользователя {user}:')
for i in response.json():
    print(i['name'])

'''
Ответ:
bitcoin-master
drupal-8.1.3
helloworld
tensorflow
'''
