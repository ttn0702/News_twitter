from peewee import *
import requests
from File_Class import File_Interact

host='45.76.187.125'
db_name = 'tw_crawl'
db_user='nghiahsgs4'
db_pass='261997'
db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)
list_link = []
list_url_img = []
list_content_text = []
# model tuong ung voi table
class Channel(Model):
    link = CharField()
    nb_follower = CharField()
    nb_following = CharField()
    class Meta:
        database=db

class Post(Model):
    channel_id = CharField() 
    link_post = CharField()
    content_text = TextField()
    url_image = CharField()
    class Meta:
        database=db


if __name__ == "__main__":
    Channel.create_table()
    Post.create_table()
#     data_source = [
#         {
#             'link' : list_link[i],
#             'nb_follower' : l
#         }
#         for i in range(len(list_link))
#     ]

# for batch in chunked(data_source,10000):
#     Channel.insert_many(batch).execute()