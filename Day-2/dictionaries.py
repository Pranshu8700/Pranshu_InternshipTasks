# how to create dictionaries
user = {'name' : 'Pranshu', 'age' : '19'}
print(user)
print(type(user))

user1 = dict(name = 'Pranshu', age = 19)
print(user1)

# how to access data from dictionary
print(user['name']) # key

# which data can be stored in dictionary ? 
# anything 
# user_info = {
#     'name' : 'Pranshu',
#     'Age' : 20,
#     'fav_movies' : ['URI', 'PK'],
#     'fav_tunes' : ['Pachtaoge', 'mafiyaan'], 
#     }
# print(user_info['fav_movies'])

# users  = {
#     user1 : {'name' : 'Pranshu',
#     'Age' : 20,
#     'fav_movies' : ['URI', 'PK'],
#     'fav_tunes' : ['Pachtaoge', 'mafiyaan'],
#     }
# }

# how to add data in empty dictionary
user_info2 = {}
user_info2['name'] = 'Pranshu'
print(user_info2)
x = user['name']
print(x)
