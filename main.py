from selenium import webdriver
from bs4 import BeautifulSoup

def divider_tag(tag):
    return tag[tag.find('>') + 1:tag.find('</')]

def get_number():
    url = 'chromedriver.exe'
    driver = webdriver.Chrome(url)

    driver.get('https://www.receivesms.co/active-numbers/')

    html_source_code = driver.execute_script("return document.body.innerHTML;")
    bs = BeautifulSoup(html_source_code, 'html.parser')

    phones = bs.findAll('a', {'class' : 'btn'})
    receive_links = bs.findAll('a', {'target' : '_self'})

    website = 'https://www.receivesms.co/'

    for i in range(len(phones)):
        phones[i] = divider_tag(str(phones[i]))
        receive_links[i] = website + receive_links[i].get('href')

    return [phones, receive_links]

