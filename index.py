from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import *

list_link = []
list_url_img = []
list_content_text = []
link = 'https://twitter.com/OKEx?s=20'

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# nb_followers nb_following
err1,nb_followers,nb_following = get_info_twitter(driver,link)


# Chanel_ID
chanel_id = get_channel_id(link)

# Get info post
err2,list_link,list_url_img,list_content_text = get_info_post(driver,link)