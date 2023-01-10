from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


#open browser
browser = webdriver.Firefox()

browser.get('https://drive.google.com/drive/u/0/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')

#get in the folder
folder = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'jGNTYb')))
browser.find_element(By.CLASS_NAME, 'jGNTYb').click()

#download excel table
download = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'BABID'))) 
browser.find_element(By.CSS_SELECTOR, '.akerZd > svg:nth-child(1) > path:nth-child(1)').click()

time.sleep(5)

#get excel table
table = pd.read_excel(r'C:\Users\OLIWER\Downloads\Vendas - Dez.xlsm')
#print(sells)

#open email  
browser.get('https://account.proton.me/login')
login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'username')))
browser.find_element(By.ID, 'username').send_keys('olwrrb@protonmail.com') #enter user info
browser.find_element(By.ID, 'password').send_keys('Shabh319ggl0lm@ocorpsux') #enter password info
browser.find_element(By.CSS_SELECTOR, 'button.button:nth-child(6)').click()

time.sleep(20)

#create new mail
new_mail = WebDriverWait(browser, 15).until(EC.element_to_be_clickable)((By.CSS_SELECTOR, '.button-large'))
browser.find_element(By.CSS_SELECTOR, '.button-large').click()
browser.find_element(By.ID, 'to-composer-990').send_keys('benites.olvr@gmail.com') #enter email address
browser.find_element(By.ID, 'subject-composer-925').send_keys('python fooling around') #add subject

#add attachment
attachment = browser.find_element(By.CSS_SELECTOR, 'label.button').click() 
#send email
