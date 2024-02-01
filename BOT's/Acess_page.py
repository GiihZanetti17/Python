from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime


#variables
delay = 9
name = 'xxxx'
user = 'xxxxx'
password = 'xxxxx'
month = datetime.now().month

if month == 1:
    month = 13

url = 'https://xxxxxx/xxxxxx/xxxxxxx/xxxxxxxxxx.php?xxxx=x&xxxxx=xxxxx&xxxxxx=&date={}'.format(datetime.now().year)+'{:02d}'.format(month-1)
nav = webdriver.Firefox()

    
#Open the site
nav.get (url)

#Login
nav.find_element(By.NAME,'username').send_keys(user)
nav.find_element(By.NAME,'userpass').send_keys(password)
nav.find_element(By.ID,'submit').click()

sleep(delay)

#Download PDF
nav.find_element(By.ID, 'download').click()
