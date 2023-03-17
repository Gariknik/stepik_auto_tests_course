import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
import time


calc = lambda x: str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    res = calc(num)
    input_res = browser.find_element(By.ID, 'answer')
    input_res.send_keys(res)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    option_r = browser.find_element(By.ID, "robotsRule")
    option_r.click()
    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()
    time.sleep(2)
    alert_t = browser.switch_to.alert
    print(alert_t.text.split(': ')[1])
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()