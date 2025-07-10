from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

group_links_list = [
    "https://www.facebook.com/groups/1044594397668306",
    "https://www.facebook.com/groups/1044594397668306",
    ]
message = """
Hello, this is a test message,just take a look at this video
link:https://youtu.be/H1YG3ipxl20?si=onap9SOdQ7IM9MY-
"""
photo = 'MacRock.png'

options= webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('C:\\Users\\Admin\\ppData\\Local\\Google\\Chrome\\User Data')
options.binary_location('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get('https://www.facebook.com')

def main():
    for group in group_links_list:
        driver.get(group)
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR,'._1mf._1mj').click()
        time.sleep(20)
        photo_element = driver.find_element(By.CSS_SELECTOR,'._1mf._1mj')
        photo_element.send_keys(photo)
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR,'._1mf._1mj').send_keys(message)
        time.sleep(20)
        post_button = driver.find_element(By.CSS_SELECTOR,'._1mf._1mj')
        post_button.click()
        time.sleep(20)
    driver.close()
    print('posted')
    
if __name__ == '__main__':
    main()
        
        



