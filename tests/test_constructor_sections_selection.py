import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestConstructorSections:

    def setup_method(self):
        self.email = "Semenov_Dmitry_15_QA_FS_275@mail.ru"
        self.correct_password = "sd15qafs"

    def test_constructor_buns_button_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        time.sleep(2)   # Выставлен тайм-аут, т.к. проверки 50/50 без тайминга проходят с ошибкой, не успевает форма загрузиться
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_BUTTON).click()   # Здесь единственный вариант, где необходимо инициализировать
        # переключение на сторонний раздел "Соусы", т.к. страница изначально открывается на разделе "Булки"
        driver.find_element(By.XPATH, Locators.BUNS_BUTTON).click()
        time.sleep(2)   # Здесь выставляем специально задержку на скролл, т.к. если без задержки результат "Соусы", скролл не успевает за тестом
        selected_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SELECTED_SECTION).text   # Создаем переменную, которая
        # содержит текст/название текущего выбранного раздела.
        # Локатор CONSTRUCTOR_SELECTED_SECTION содержит код !!ИМЕННО ВЫБРАННОГО РАЗДЕЛА!! специально смотрел в html как реагирует код
        # при переключении разделов - в класс дописывается "tab_tab_type_current__2BEPc" именно при выборе раздела
        assert selected_section == "Булки"
        driver.quit()

    def test_constructor_sauces_button_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_BUTTON).click()
        time.sleep(2)
        selected_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SELECTED_SECTION).text
        assert selected_section == "Соусы"
        driver.quit()

    def test_constructor_fillings_button_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.XPATH, Locators.FILLINGS_BUTTON).click()
        time.sleep(2)
        selected_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SELECTED_SECTION).text
        assert selected_section == "Начинки"
        driver.quit()
