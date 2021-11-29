from selenium import webdriver
from utils import *
from utils_db import *
from peewee import *
from File_Class import *

# File_Interact1 = File_Interact('link_twitter.txt')
File_Interact1 = File_Interact('text.txt')
list_tw =File_Interact1.read_file_list()

list_nb_followers = []
list_nb_following = []

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

for link in list_tw:
    # nb_followers nb_following
    err1,nb_followers,nb_following = get_info_twitter(driver,link)
    list_nb_followers.append(nb_followers)
    list_nb_following.append(nb_following)
driver.quit()

data_source = [
        {
            'link' : list_tw[i],
            'nb_follower' : list_nb_followers[i],
            'nb_following' : list_nb_following[i]
        }
        for i in range(len(list_tw))
    ]
    
# for batch in chunked(data_source,10000):
#     Channel.insert_many(batch).execute()
