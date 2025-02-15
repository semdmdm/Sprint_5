import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

# все тесты советую запускать с впн, т.к. с ним гораздо быстрее это происходит, без впн - присутствует
# задержка секунд в 10-15 между открытием браузера (главной страницы сервиса) и запуском шагов теста внутри браузера
# Хотел добавить рандом чисел в генерирование email, но потом понял, что будет рандомить во всех места,
# а надо чтобы при регистрации и логине были одинаковые 3 цифры в email

class TestRegistration:

    def test_registration_incorrect_password_error_Chrome(self, driver, data):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_PERSONAL_ACCOUNT_PAGE).click()
        driver.find_element(By.XPATH, Locators.NAME_INPUT_REGISTRATION).send_keys(data["name"])
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT_REGISTRATION).send_keys(data["email_random"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT_REGISTRATION).send_keys(data["incorrect_password"])
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_REGISTER_PAGE).click()
        error = driver.find_element(By.XPATH, Locators.ERROR_MESSAGE).text
        assert error == "Некорректный пароль"

    def test_succesfull_registration_Chrome(self, driver, data):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_PERSONAL_ACCOUNT_PAGE).click()
        driver.find_element(By.XPATH, Locators.NAME_INPUT_REGISTRATION).send_keys(data["name"])
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT_REGISTRATION).send_keys(data["email_random"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT_REGISTRATION).send_keys(data["correct_password"])
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_REGISTER_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email_random"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(data["correct_password"])
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
