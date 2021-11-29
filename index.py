from selenium import webdriver
from utils import *
from utils_db import *
from peewee import *
from File_Class import *

# File_Interact1 = File_Interact('link_twitter.txt')
File_Interact1 = File_Interact('text.txt')
list_tw =File_Interact1.read_file_list()

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

for link in list_tw:
    list_link_post = []
    list_url_img = []
    list_content_text = []
    list_channel_id = []
    # get 5 post
    err,list_link_post,list_url_img,list_content_text = get_info_post(driver,link)

    # Chanel_ID
    channel_id = get_channel_id(link)
    # list_channel_id.append(channel_id)

    data_source = [
        {
            'channel_id' : channel_id,
            'link_post' : list_link_post[i],
            'content_text' : list_content_text[i],
            'url_image' : list_url_img[i]

        }
        for i in range(0,5)
        # for i in range(len(list_link_post))
    ]
    for batch in chunked(data_source,10000):
        Post.insert_many(batch).execute()

driver.quit()