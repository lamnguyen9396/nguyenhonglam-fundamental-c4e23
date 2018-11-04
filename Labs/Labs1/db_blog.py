from pymongo import MongoClient
uri='mongodb://admin:admin1@ds121349.mlab.com:21349/c4e23-blog'

#1 Connect
client=MongoClient(uri)


#2 Get default database
db=client.get_database()

#3 Get collection
posts=db["posts"] # lazyloading
movies=db['movies']

#3 Create data
new_post={
    'title':'Hôm nay trời nắng',
    'content':'Tôi vẫn ở nhà code',
}
new_movie={
    "title":"Batman Begins",
    "rating":8.0
}
# #5 Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

# 5 Read Data
post_list=posts.find()
# p=post_list[1]
# print(p)

for p in post_list:
    print(p["title"])
    print(p["content"])
    print("------")
# #6 Close connection
# client.close()