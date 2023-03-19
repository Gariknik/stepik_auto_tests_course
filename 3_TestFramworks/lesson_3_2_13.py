import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def test_for_scenario_first(self, link="http://suninjuly.github.io/registration1.html"):
        """
        Открыть страницу с формой
        Заполнить все обязательные поля
        Заполнить все необязательные поля
        Нажать кнопку "Регистрация"
        Проверить, что есть сообщение об успешной регистрации
        """
        self.link_1 = link
        browser = webdriver.Chrome()
        browser.get(self.link_1)
        # Заполняем обязательные и необязательные поля
        element1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        element1.send_keys('Igor')
        element2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        element2.send_keys('Nik')
        element3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        element3.send_keys('Nik@mail.ru')
        element4 = browser.find_element(By.XPATH, '//div[@class="second_block"]//div/input[@class="form-control first"]')
        element4.send_keys('780956362734')
        element5 = browser.find_element(By.XPATH, '//div[@class="second_block"]//div/input[@class="form-control second"]')
        element5.send_keys('Russia')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be text 'Congratulations! You have successfully registered!'")


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_for_scenario_second(self, link="http://suninjuly.github.io/registration2.html"):
        """
        Открыть страницу с формой
        Заполнить все обязательные поля
        Заполнить все необязательные поля
        Нажать кнопку "Регистрация"
        Проверить, что есть сообщение об успешной регистрации
        """
        self.link_2 = link
        browser = webdriver.Chrome()
        browser.get(self.link_2)
        # Заполняем обязательные и необязательные поля
        element1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        element1.send_keys('Igor')
        element2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        element2.send_keys('Nik')
        element3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        element3.send_keys('Nik@mail.ru')
        element4 = browser.find_element(By.XPATH, '//div[@class="second_block"]//div/input[@class="form-control first"]')
        element4.send_keys('780956362734')
        element5 = browser.find_element(By.XPATH, '//div[@class="second_block"]//div/input[@class="form-control second"]')
        element5.send_keys('Russia')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be text 'Congratulations! You have successfully registered!'")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()