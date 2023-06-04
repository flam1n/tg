from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

def parser(numb):
    links = ['https://youtube.com/@marinadushenova']

    while True:
        driver = webdriver.Chrome('chromedriver.exe')
        title = ''
        desc = ''
        data = []
        try:
            for i in links:
                driver.get(i)
                sleep(20)
                link_ = []

                for k in driver.find_elements(By.ID, 'dismissible'):
                    link_.append(k.find_element(By.ID, 'thumbnail').get_attribute('href'))
                    if len(link_) >= numb:
                        break

                for k in link_:
                    driver.get(k)
                    sleep(15)
                    driver.find_element(By.CSS_SELECTOR, 'tp-yt-paper-button#more.style-scope.ytd-expander').click()

                    res = driver.find_elements(By.CSS_SELECTOR, 'he.title.style-scope.ytd-video-primary-info-renderer')

                    for j in res:
                        if j.text != '':
                            desc = j.text
                            break

                    data.append([ k, title, desc])
            driver.close()



        except Exception as e:
            print(e)
            driver.close()