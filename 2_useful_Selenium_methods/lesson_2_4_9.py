import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = 'http://suninjuly.github.io/explicit_wait2.html'
func = lambda x: math.log(abs(12 * math.sin(x)))
try:
    bro = webdriver.Chrome()
    bro.get(link)

    el = WebDriverWait(bro, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    bro.find_element(By.ID, 'book').click()
    bro.execute_script("window.scrollBy(0, 100);")
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
