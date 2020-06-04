'''
2. Изучить список открытых API. Найти среди них любое,
требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию.
Ответ сервера записать в файл.
'''
import requests
import json

# access token и client_id генерируются на сайте https://twitchtokengenerator.com/, нужно создать аккаунт на twitch
# и после на этом сайте дать доступ и получить это. Первый раз этим занялся, честно говоря намучился ))) но очень
# интересно, спасибо за такие задания! Оказалось, что токен на Twitch получить очень не просто, если не
# прибегнуть к данному методу. Там можно apps создавать, но честно говоря не разобрался как можно это сделать
# другим путем.

headers = {'Authorization': 'Bearer ACCESS_TOKEN',
           'Client-ID': 'CLIENT_ID'}
r = requests.get('https://api.twitch.tv/helix/games/top', headers=headers, stream=True)

# сохранил в файл json
with open('twitch.json', 'w') as output_file:
    output_file.write(r.text)

# загрузил из файла json
with open('twitch.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)

top_games_twitch = []
for i in templates:
    if i == 'data':
        for z in templates[i]:
            top_games_twitch.append([z['name'], z['id']])

for i in top_games_twitch:
    print(*i)

'''
Ответ:
Just Chatting 509658
Counter-Strike: Global Offensive 32399
Grand Theft Auto V 32982
Fortnite 33214
League of Legends 21779
Minecraft 27471
Call of Duty: Modern Warfare 512710
VALORANT 516575
World of Warcraft 18122
FIFA 20 512804
Dota 2 29595
Escape From Tarkov 491931
Apex Legends 511224
Poly Bridge 2 517320
Hearthstone 138585
Slots 498566
Golf It! 495764
Tom Clancy's Rainbow Six: Siege 460630
Overwatch 488552
Chess 743
'''
