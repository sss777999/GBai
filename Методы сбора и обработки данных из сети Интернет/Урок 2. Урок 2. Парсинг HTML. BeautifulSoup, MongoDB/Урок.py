import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

main_link = 'https://www.kinopoisk.ru'
params = {'quick_filters':'serials'}

response = requests.get(main_link + '/popular/', params=params)
soup = bs(response.text, 'lxml')

serials_block = soup.find('div', {'class':'selection-list'})

serials_list = serials_block.findChildren(recursive=False)

serials = []

for serial in serials_list:
    serial_data = {}
    tag_link = serial.find('a', {'class':'selection-film-item-meta__link'})
    link = main_link + tag_link['href']
    name = tag_link.findChild().text

    genre = serial.find('span', {'class':'selection-film-item-meta__meta-additional-item'}).nextSibling.text
    rating = float(serial.find('span', {'class':'rating__value'}).text)

    serial_data['name'] = name
    serial_data['link'] = link
    serial_data['genre'] = genre
    serial_data['rating'] = rating

    serials.append(serial_data)

pprint(serials)






