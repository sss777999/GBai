import pymongo

# запросы к бд 4, 5 пункт

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["inst_users_parser"]
mycol = mydb["instagram"]

# 4
subscribers = mycol.find({'username': 'fight_.wear', 'user_id_subscribers': {'$exists': True}},
                         {'info_full_user_name': 1, 'info_user_name': 1, })
print(f'Subscribers of fight_.wear user:')
for _, i in enumerate(subscribers):
    print(_, i)
print(subscribers)

print()
print('*' * 130)
print()

# 5
follows = mycol.find({'username': 'fight_.wear', 'follow_by_user_id': {'$exists': True}},
                     {'info_full_user_name': 1, 'info_user_name': 1, })
print(f'Follows of fight_.wear user:')
for _, i in enumerate(follows):
    print(_, i)
print(follows)
