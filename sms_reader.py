import receive_number
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def divider_tag(tag):
    return tag[tag.find('>') + 1:tag.find('</')]


def get_sms(number_of_phone):
    url = 'chromedriver.exe'
    driver = webdriver.Chrome(url)

    phone_link = receive_number.get_number()[1][number_of_phone]

    #for link in phone_links:
    #for i in range(2):
    run = True
    while run:
        #driver.get(link)
        driver.get(phone_link)
        html_source_code = driver.execute_script("return document.body.innerHTML;")
        bs = BeautifulSoup(html_source_code, 'html.parser')

        sms = bs.findAll('div', {'class' : 'col-xs-12'})
        for j in range(len(sms)):
            sms[j] = str(sms[j].text)
            if 'ویرگول' in sms[j]:
                run = False
                virgool_sms = sms[j]
            #print(sms[j])
        time.sleep(2)

    return virgool_sms





