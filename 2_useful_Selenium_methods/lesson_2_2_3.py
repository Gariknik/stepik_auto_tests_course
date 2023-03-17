from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    bro = webdriver.Chrome()
    bro.get(link)
    num1 = int(bro.find_element(By.ID, 'num1').text)
    num2 = int(bro.find_element(By.ID, 'num2').text)
    res = num1 + num2
    select = Select(bro.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(res))
    btn = bro.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()
    time.sleep(2)
    alert_t = bro.switch_to.alert
    print(alert_t.text.split(': ')[1])
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    bro.quit()