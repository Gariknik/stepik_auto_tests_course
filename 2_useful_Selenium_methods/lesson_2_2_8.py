from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
path_file = os.path.abspath(os.path.dirname(__file__))
all_path_file = os.path.join(path_file, 'me.txt')
try:
    bro = webdriver.Chrome()
    bro.get(link)
    name = bro.find_element(By.CSS_SELECTOR, '[name = "firstname"]').send_keys('Igor')
    surname = bro.find_element(By.CSS_SELECTOR, '[name = "lastname"]').send_keys('Nik')
    mail = bro.find_element(By.CSS_SELECTOR, '[name = "email"]').send_keys('Nik@gmail.com')

    put_file = bro.find_element(By.ID, 'file').send_keys(all_path_file)

    btn = bro.find_element(By.XPATH, '//button[@type = "submit"]').click()

    time.sleep(2)
    a_t = bro.switch_to.alert
    print(a_t.text.split(': ')[1])
finally:
    time.sleep(5)
    bro.quit()