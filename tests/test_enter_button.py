import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestEnterButton:

    def setup_method(self):
        self.email = "Semenov_Dmitry_15_QA_FS_275@mail.ru"
        self.correct_password = "sd15qafs"


    def test_enter_button_main_page_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_MAIN_PAGE).click()
        time.sleep(2) # Тут немного иная проблема почему выставлен sleep, если его не выставлять начинают
        # параллельно запускаться 2-3 окна Chrome и начинают возникать ошибки как я понимаю из-за
        # запараллеливания тестов (работает только с импортированием time)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
        driver.quit()


    def test_enter_button_personal_account_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
        driver.quit()


    def test_enter_button_registration_form_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_PERSONAL_ACCOUNT_PAGE).click()
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_REGISTRATION_FORM).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
        driver.quit()


    def test_enter_button_password_recovery_form_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.RECOVERY_PASSWORD_BUTTON).click()
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PASSWORD_RECOVERY_FORM).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
        driver.quit()
