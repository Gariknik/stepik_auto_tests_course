import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/alert_accept.html'
func = lambda x: math.log(abs(12 * math.sin(x)))
try:
    bro = webdriver.Chrome()
    bro.get(link)

    bro.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
    alert_w = bro.switch_to.alert
    alert_w.accept()

    num = bro.find_element(By.ID, 'input_value').text
    res = func(int(num))
    inp = bro.find_element(By.ID, 'answer')
    inp.send_keys(res)
    bro.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
    alert_t = bro.switch_to.alert
    print(alert_t.text.split(': '))

finally:
    time.sleep(5)
    bro.quit()