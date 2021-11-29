from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_channel_id(link):
    return link.replace('?s=20','').split('/')[-1]

def get_info_twitter(driver,link):
    nb_followers = ''
    nb_following = ''
    try:
        driver.get(link)
        try:
            WebDriverWait(driver , 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="/{get_channel_id(link)}/following"]')))
            js_nb_following = f'''return document.querySelectorAll('a[href="/{get_channel_id(link)}/following"]')[0].innerText'''
            nb_following = driver.execute_script(js_nb_following).split(' ')[0]
        except:
            WebDriverWait(driver , 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="css-4rbku5 css-18t94o4 css-901oao r-18jsvk2 r-1loqt21 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"]')))
            js_nb_following = f'''return document.querySelectorAll('a[class="css-4rbku5 css-18t94o4 css-901oao r-18jsvk2 r-1loqt21 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"]')[0].innerText'''
            nb_following = driver.execute_script(js_nb_following).split(' ')[0]
        try:
            WebDriverWait(driver , 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="/{get_channel_id(link)}/followers"]')))
            js_nb_followers = f'''return document.querySelectorAll('a[href="/{get_channel_id(link)}/followers"]')[0].innerText'''
            nb_followers = driver.execute_script(js_nb_followers).split(' ')[0]
        except:
            WebDriverWait(driver , 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="css-4rbku5 css-18t94o4 css-901oao r-18jsvk2 r-1loqt21 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"]')))
            js_nb_following = f'''return document.querySelectorAll('a[class="css-4rbku5 css-18t94o4 css-901oao r-18jsvk2 r-1loqt21 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"]')[1].innerText'''
            nb_following = driver.execute_script(js_nb_following).split(' ')[0]

        return '',nb_followers,nb_following
    except Exception as err:
        print(err)
        return err,nb_followers,nb_following

def get_info_post(driver,link):
    count = 0
    Y = 100
    try:
        driver.get(link)
        list_link = []
        list_url_img = []
        list_content_text = []
        WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l"]')))
        time.sleep(3)
        while len(list_link) < 5:
            js = '''return document.querySelectorAll('div[class="css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l"]').length'''
            len_ele = driver.execute_script(js)
            for index in range(len_ele):
                # print('index: ',index)
                # Get link post
                js_link_post= f'''return document.querySelectorAll('div[class="css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l"]')[{index}].querySelectorAll('a[class="css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0"]')[0].href'''
                link_post = driver.execute_script(js_link_post)
                if link_post not in list_link:
                    try:
                        # Get conntent text
                        js_content_text = f'''return document.querySelectorAll('div[class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')[{index}].innerText'''
                        content_text = driver.execute_script(js_content_text)
                    except:
                        content_text = ''
                    # Get url image
                    url_img = ''
                    js_img = f'''return document.querySelectorAll('div[class="css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l"]')[{index}].querySelectorAll('img[alt="Image"]').length'''
                    len_img = driver.execute_script(js_img)
                    if len_img != 0:
                        for j in range(len_img):
                            js_src_img = f'''return document.querySelectorAll('div[class="css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l"]')[{index}].querySelectorAll('img[alt="Image"]')[{j}].src'''
                            url_img = url_img + driver.execute_script(js_src_img) + ' '  

                    if content_text != '' or url_img != '':
                        list_url_img.append(url_img)
                        list_content_text.append(content_text)
                        list_link.append(link_post)
                        count = 0
                    else:
                        continue
                    if len(list_link) >= 5:
                        break
                    print(len(list_link))
                else:
                    count += 1
                    continue
            # Dùng biến count để chống bị đứng chương trình trường hợp(Channel không đủ 5 bài đăng)
            if count == 10000:
                break
            js = f'''window.scroll(0,{Y})'''
            driver.execute_script(js)
            Y += 20

        return '',list_link,list_url_img,list_content_text
    except Exception as err:
        print(err)
        return err,list_link,list_url_img,list_content_text
        