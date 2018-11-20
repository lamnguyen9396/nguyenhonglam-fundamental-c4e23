from pymongo import MongoClient
uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client=MongoClient(uri)

db=client.get_database()

posts=db["posts"]

new_post={
    'title':'Cảm nhận',
    'author':'Lâm',
    'content':'Lớp vui, giáo viên và các bạn giảng viên rất giỏi và nhiệt tình :D',
}

posts.insert_one(new_post)
