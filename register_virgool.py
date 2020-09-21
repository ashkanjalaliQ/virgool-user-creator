from selenium import webdriver
import receive_number
import sms_reader
import random
import time
import names
import re
import name_creator

url = 'chromedriver.exe'
driver = webdriver.Chrome(url)

driver.get('https://virgool.io/register')
driver.maximize_window()

##register in virgool
number_of_phone = 15

phone_numbers = receive_number.get_number()[0][number_of_phone]


print(phone_numbers)
driver.find_element_by_xpath('//*[@id="react-app"]/main/section[2]/section/aside/div[1]/input').send_keys(phone_numbers)
driver.find_element_by_xpath('//*[@id="react-app"]/main/section[2]/section/aside/div[2]/button').click()

time.sleep(8)

verification_code = sms_reader.get_sms(number_of_phone)
verification_code = re.search(r'\d+', verification_code).group()
print(verification_code)


for i in range(len(verification_code)):
    driver.find_element_by_xpath('//*[@id="react-app"]/main/section[2]/section/div[3]/div/div[' + str(i + 1) + ']/input').send_keys(verification_code[i])
    #driver.find_element_by_xpath('//*[@id="react-app"]/main/section[2]/section/div[3]/div/div[2]/input').send_keys()

time.sleep(10)

random_name = name_creator.get_name()
driver.find_element_by_xpath('//*[@id="react-app"]/main/section[2]/div/div/div[2]/input').send_keys(random_name)
driver.find_element_by_xpath('//*[@id="react-app"]/main/section[2]/div/div/div[3]/button').click()

time.sleep(10)

##//*[@id="react-app"]/main/section[2]/div/div/div[2]/input

##//*[@id="react-app"]/main/section[2]/div/div/div[3]/button

driver.find_element_by_xpath('//*[@id="react-app"]/div/div[2]/div/div/button').click()

for i in range(6):
    driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div[' + str(i + 1) + ']').click()
    time.sleep(1)
time.sleep(1)
driver.find_element_by_class_name('btn-main').click()

time.sleep(20)

#driver.find_element_by_xpath('/html/body/section/header/section/section/div[2]/section/div[2]/div[3]/div').click()
driver.find_element_by_class_name('toggle--big').click()
driver.find_element_by_xpath('/html/body/section/header/section/section/div[2]/section/div[2]/div[3]/ul/li[3]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="edit-profile-form"]/div[2]/section/section/aside[1]/label/div/button[1]').click()

username = names.get_full_name().replace(' ', '').lower() + str(random.randint(11111, 99999))
print(username)
#driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="username"]').clear()
driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
time.sleep(5)

driver.find_element_by_xpath('//*[@id="edit-profile-form"]/div[2]/section/section/aside[1]/label/div/button[2]').click()
time.sleep(5)

driver.find_element_by_class_name('toggle--big').click()
driver.find_element_by_xpath('/html/body/section/header/section/section/div[2]/section/div[2]/div[3]/ul/li[3]/a').click()
time.sleep(5)
password = '20052005'
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
time.sleep(0.5)
driver.find_element_by_css_selector('#edit-profile-form > div.listview-content.clearfix > section > section > div > button').click()
time.sleep(10)