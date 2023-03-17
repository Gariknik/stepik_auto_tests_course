import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/execute_script.html'
func = lambda x: math.log(abs(12 * math.sin(x)))
try:
    bro = webdriver.Chrome()
    bro.get(link)

    bro.execute_script("window.scrollBy(0, 100);")

    num = int(bro.find_element(By.ID, 'input_value').text)
    res = func(num)
    inp = bro.find_element(By.ID, 'answer')
    inp.send_keys(res)
    check = bro.find_element(By.CSS_SELECTOR, '[for = "robotCheckbox"]').click()
    opt = bro.find_element(By.CSS_SELECTOR, '[for = "robotsRule"]').click()
    btn = bro.find_element(By.XPATH, '//button[@type = "submit"]').click()
    time.sleep(2)
    alert_t = bro.switch_to.alert
    print(alert_t.text.split(': ')[1])
    time.sleep(10)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    bro.quit()